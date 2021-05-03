import asyncio
import time

from aiocache import cached


@cached()
async def fibn(n):
    if n in (0, 1):
        return n
    return await fibn(n - 2) + await fibn(n - 1)


start = time.time()
loop = asyncio.get_event_loop()
c = loop.run_until_complete(fibn(100))
end = time.time()
print(f'{end-start} secs')
