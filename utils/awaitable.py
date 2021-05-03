from functools import wraps
import asyncio

from from_coro import from_coro


def awaitable(syncfunc):
    def decorate(asyncfunc):
        @wraps(asyncfunc)
        def wrapper(*args, **kwargs):
            if from_coro(2):
                return asyncfunc(*args, **kwargs)
            else:
                return syncfunc(*args, **kwargs)
        return wrapper
    return decorate


def spam():
    print("The blue pill")


@awaitable(spam)
async def spam():
    print('The red pill')


async def main():
    await spam()

if __name__ == '__main__':
    spam()
    asyncio.run(main())
