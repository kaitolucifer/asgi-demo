import trio


async def proxy_one_way(source, sink):
    while True:
        data = await source.receive_some(1024)
        if not data:
            await sink.send_eof()
            break
        await sink.send_all(data)


async def proxy_two_way(a, b):
    async with trio.open_nursery() as nursery:
        nursery.start_soon(proxy_one_way, a, b)
        nursery.start_soon(proxy_one_way, b, a)


async def main():
    with trio.move_on_after(10):
        a = await trio.open_tcp_stream("localhost", 12345)
        b = await trio.open_tcp_stream("localhost", 54321)
        async with a, b:
            await proxy_two_way(a, b)
    print("all done!")


if __name__ == '__main__':
    trio.run(main)
