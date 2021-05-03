from functools import wraps
import asyncio

from from_coro import from_coro


def sync_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if from_coro(2):
            raise RuntimeError("Can't call from coroutine")
    return wrapper


@sync_only
def spam():
    print('Hello Guido')


async def main():
    spam()


if __name__ == '__main__':
    spam()
    asyncio.run(main())
