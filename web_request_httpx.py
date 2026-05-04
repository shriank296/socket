import asyncio

import httpx

from utils.practice_decorator import async_timed

# limits = httpx.Limits(max_connections=500, max_keepalive_connections=200)


@async_timed()
async def fetch(client, url):
    r = await client.get(url)

    return r.status_code


@async_timed()
async def main():
    urls = ["http://example.com" for _ in range(1000)]

    async with httpx.AsyncClient(timeout=50) as client:
        tasks = [fetch(client, url) for url in urls]

        results = await asyncio.gather(*tasks)

    print(results)


asyncio.run(main())
