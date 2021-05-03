import asyncio


@asyncio.coroutine
def test1():
    print(1)
    yield gen2.send(None)
    print('test1 done')


def test2():
    print(2)
    yield


gen1 = test1()
gen2 = test2()
asyncio.run(gen1)
