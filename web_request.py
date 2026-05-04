import asyncio

import niquests
from niquests import AsyncSession

from utils import async_timed

# s = AsyncSession(multiplexed=True)


# @async_timed()
# async def fetch_status(url: str) -> int:
#     async with AsyncSession() as session:
#         result = await session.get(url)

#         return result.status_code


# @async_timed()
# async def main():
#     urls = ["https://www.example.com" for _ in range(1000)]

#     async with AsyncSession() as session:
#         tasks = [fetch_status(session, url) for url in urls]

#         status_codes = await asyncio.gather(*tasks)

#     print(status_codes)


# @async_timed()
# async def fetch_status(url: str) -> int:
#     r = await niquests.aget(url)
#     return r.status_code


# @async_timed()
# async def main():
#     urls = ["https://www.example.com" for _ in range(1000)]

#     tasks = [fetch_status(url) for url in urls]

#     status_codes = await asyncio.gather(*tasks)

#     print(status_codes)


# @async_timed()
# async def fetch_status(session, url):
#     r = await session.get(url)

#     return r.status_code


# @async_timed()
# async def main():
#     urls = ["https://www.example.com" for _ in range(1000)]

#     async with AsyncSession() as session:
#         tasks = [fetch_status(session, url) for url in urls]

#         results = await asyncio.gather(*tasks)

#     print(results)


@async_timed()
async def main():
    async with AsyncSession(multiplexed=True) as session:
        # Step 1: schedule requests (coroutines)

        coros = [session.get("https://www.example.com") for _ in range(1000)]

        # Step 2: run them concurrently → get lazy responses

        lazy_responses = await asyncio.gather(*coros)

        # Step 3: resolve all responses via session

        responses = await session.gather(*lazy_responses)

        status_codes = [r.status_code for r in responses]

    print(status_codes)


asyncio.run(main())
