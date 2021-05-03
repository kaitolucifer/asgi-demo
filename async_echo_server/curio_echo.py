from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from curio import spawn, run, tcp_server
from curio.socket import socket


async def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    sock.bind(address)
    sock.listen(5)
    while 1:
        client, addr = await sock.accept()
        await spawn(echo_handler(client, addr))


async def echo_handler(client, addr):
    print(f"Connection from {addr}")
    async with client:
        while 1:
            data = await client.recv(4096)
            if not data:
                break
            await client.sendall(data)
    print("Connection closed")


if __name__ == '__main__':
    # run(echo_server(('', 25000)))
    run(tcp_server('', 25000, echo_handler))
