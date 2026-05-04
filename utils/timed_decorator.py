import functools
import time
from collections.abc import Callable
from typing import Any


def async_timed():  # this async timed is extra it is needed when we want to pass argument to async_timed
    """
    Below is how it works.

    @async_timed
    def async fetch_data(x,y):
        return x + y

    fetch_data = async_timed()fetch_data

    """

    def wrapper(func: Callable):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print("Starting {func} with args {args} {kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"finished {func} in {total} seconds.")

        return wrapped

    return wrapper
