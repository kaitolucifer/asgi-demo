from socket import socket, AF_INET, SOCK_STREAM
import time


def benchmark(addr, nmessages):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(addr)
    start = time.time()
    for n in range(nmessages):
        sock.send(b"x")
        _ = sock.recv(4096)
    end = time.time()
    print(f'{nmessages/(end-start)} messages/sec')


if __name__ == '__main__':
    benchmark(('localhost', 25000), 100000)
