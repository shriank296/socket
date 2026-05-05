import asyncio
import niquests

from utils.practice_decorator import async_timed


@async_timed()
async def fetch(session, url):
    resp = await session.get(url)
    return resp.status_code


@async_timed()
async def main():
    async with niquests.AsyncSession() as session:
        urls = ["http://example.com" for _ in range(1000)]

        tasks = [fetch(session, url) for url in urls]

        results = await asyncio.gather(*tasks)

    print(results)


asyncio.run(main())
