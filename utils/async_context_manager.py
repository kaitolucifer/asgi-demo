import asyncio


async def coro():
    print('coro')


class AsyncManager:
    async def __aenter__(self):
        print("Entering")
        await coro()
        return self

    async def __aexit__(self, ty, val, tb):
        print("Exiting")
        await coro()


async def main():
    am = AsyncManager()
    async with am as m:
        print(m)

if __name__ == '__main__':
    asyncio.run(main())
