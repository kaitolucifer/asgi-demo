import asyncio


async def coro():
    print('coro')


class AsyncCountDown:
    def __init__(self, n):
        self.n = n

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.n < 1:
            raise StopAsyncIteration
        await coro()
        self.n -= 1
        return self.n + 1


async def main(n):
    c = AsyncCountDown(n)
    async for i in c:
        print(i)

if __name__ == '__main__':
    asyncio.run(main(10))
