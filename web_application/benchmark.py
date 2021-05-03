import asyncio
import time

import aiohttp
import uvloop


async def fetch(session, host):
    async with session.get(host) as response:
        response = await response.read()
        return response


async def fetch_many(host, n):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, host) for _ in range(n)]
        responses = await asyncio.gather(*tasks)
        return responses


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    n_msgs = 10000
    host = 'http://0.0.0.0'
    start = time.time()
    asyncio.run(fetch_many(host, n_msgs))
    elapsed_time = time.time() - start
    print(f"{(n_msgs/elapsed_time):.2f}[messages/sec]")
