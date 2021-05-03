import subprocess

from curio import run
from curio.io import FileStream


p = subprocess.Popen(['wc'],
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE)

if __name__ == '__main__':
    stdin = FileStream(p.stdin)
    stdout = FileStream(p.stdout)
    print(run(stdin.write(b'Hello')))
