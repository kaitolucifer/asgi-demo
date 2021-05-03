import sys
import asyncio


def from_coro(n):
    return bool(sys._getframe(n).f_code.co_flags & 0x80)


def foo():
    print(from_coro(1))


async def main():
    print(from_coro(1))


if __name__ == '__main__':
    foo()
    asyncio.run(main())
