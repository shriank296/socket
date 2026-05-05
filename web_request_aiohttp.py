import asyncio

import aiohttp

from utils.practice_decorator import async_timed


@async_timed()
async def fetch(session, url):
    async with session.get(url) as resp:
        return resp.status


@async_timed()
async def main():
    # connector = aiohttp.TCPConnector(limit=200)

    async with aiohttp.ClientSession() as session:
        urls = ["https://example.com" for _ in range(1000)]

        tasks = [fetch(session, url) for url in urls]

        results = await asyncio.gather(*tasks)

    print(results)


asyncio.run(main())
