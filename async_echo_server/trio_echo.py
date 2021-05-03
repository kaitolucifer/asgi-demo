import trio


async def echo_server(server_stream):
    try:
        async for data in server_stream:
            await server_stream.send_all(b'Got: ' + data)
    except Exception as exc:
        print(f"echo server crashed: {exc}")


async def main():
    await trio.serve_tcp(echo_server, 25000)


if __name__ == '__main__':
    trio.run(main)
