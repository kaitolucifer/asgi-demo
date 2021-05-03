import asyncio


from aiocache import cached

@cached()
async def fib(n):
    if n < 2:
        return 1
    else:
        return await fib(n - 1) + await fib(n - 2)


print(asyncio.run(fib(40)))
