import subprocess


from curio import timeout_after, spawn, TaskTimeout, run
from curio.io import FileStream


async def communicate(input, stdin, stdout, timeout=None):
    stdout_task = await spawn(stdout.readall())
    try:
        async with timeout_after(timeout):
            await stdin.write(input)
            await stdin.close()
            stdout = await stdout_task.join()
        return stdout
    except TaskTimeout:
        await stdout_task.cancel()
        raise


if __name__ == '__main__':
    p = subprocess.Popen(['python'],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdin = FileStream(p.stdin)
    stdout = FileStream(p.stdout)
    p.stdin.write(b'print("stdin")\n')
    out = run(communicate(b'print("communicate")\n', stdin, stdout, 15))
    print(out.decode())
