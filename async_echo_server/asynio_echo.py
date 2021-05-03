from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import asyncio


async def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    sock.setblocking(False)
    while 1:
        client, addr = await loop.sock_accept(sock)
        print(f"Connection from {addr}")
        loop.create_task(echo_handler(client))


async def echo_handler(client):
    while 1:
        data = await loop.sock_recv(client, 4096)
        if not data:
            break
        await loop.sock_sendall(client, b'Got: ' + data)
    client.close()
    print("Connection closed")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(echo_server(('', 25000)))
    loop.run_forever()
