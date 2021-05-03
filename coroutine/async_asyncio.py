import asyncio


async def test1():
    print(1)
    await coro2
    print('test1 done')


async def test2():
    print(2)
    await asyncio.sleep(0)


coro1 = test1()
coro2 = test2()
asyncio.run(coro1)
