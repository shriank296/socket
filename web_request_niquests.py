import asyncio

from niquests import AsyncSession, Response

from utils import async_timed


@async_timed()
async def main():
    async with AsyncSession(multiplexed=True) as session:
        coros = [session.get("https://www.example.com") for _ in range(10)]

        # schedule them concurrently

        lazy_responses = await asyncio.gather(*coros)

        # now resolve them via niquests

        responses = await session.gather(*lazy_responses)

        status_codes = [r.status_code for r in responses]

    print(status_codes)


asyncio.run(main())
