import trio


async def open_tcp_socket(hostname, port, *, max_wait_time=0.250):
    targets = await trio.socket.getaddrinfo(hostname, port, type=trio.socket.SOCK_STREAM)
    failed_attempts = [trio.Event() for _ in targets]
    winning_socket = None

    async def attempt(target_idx, nursery):
        # 前のattemptの完了またはタイムアウトまで待つ
        if target_idx > 0:
            with trio.move_on_after(max_wait_time):
                await failed_attempts[target_idx - 1].wait()

        # 次のattemptをスタートする
        if target_idx + 1 < len(targets):
            nursery.start_soon(attempt, target_idx + 1, nursery)

        # 接続を試す
        try:
            *socket_config, _, target = targets[target_idx]
            socket = trio.socket.socket(*socket_config)
            await socket.connect(target)
        # もし失敗したら、次のattemptに続けよう伝える
        except OSError:
            failed_attempts[target_idx].set()
        else:
            # もし成功したら、winning socketを保存し
            nonlocal winning_socket
            winning_socket = socket
            # 他のattemptをキャンセルする
            nursery.cancel_scope.cancel()

    async with trio.open_nursery() as nursery:
        nursery.start_soon(attempt, 0, nursery)

    if not winning_socket:
        raise OSError(f'unable to connect to {hostname}:{port}')
    return winning_socket


async def main():
    print(await open_tcp_socket("amazon.com", "https"))


if __name__ == '__main__':
    trio.run(main)
