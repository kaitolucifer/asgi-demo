from gevent.server import StreamServer


def echo(socket, address):
    print(f"New connection from {address[0]}:{address[1]}")
    while 1:
        data = socket.recv(4096)
        if not data:
            break
        socket.sendall(b'Got: ' + data)
    socket.close()


if __name__ == '__main__':
    server = StreamServer(('localhost', 25000), echo)
    server.serve_forever()
