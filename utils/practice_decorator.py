import functools
import time
from collections.abc import Callable

"""
produce this result.

@log_calls
def add(a, b):
    return a + b


Calling add with (2, 3)

Returned 5
"""


# def log_calls(func: Callable):
#     @functools.wraps(func)
#     def wrapper(*args):
#         print(f"Calling add with {args}")
#         try:
#             total = func(*args)
#             return total
#         finally:
#             print(f"Returned {total}")

#     return wrapper


# @log_calls
# def add(a, b):
#     return a + b


# add(2, 3)


"""
Create decorator which count calls.

@count_calls
def greet():

    print("hi")
"""


# def count_calls(
#     func: callable,
# ):  # count calls is not executed on every func call. It is executed once when fucntion is defined. That is why calls value keeps on increasing on each call to greet.
#     calls = 0

#     @functools.wraps(func)
#     def wrapper(*args, **kwars):
#         nonlocal calls
#         calls += 1
#         try:
#             func(*args, **kwars)
#         finally:
#             print(f" Call #{calls}")

#     return wrapper


# @count_calls
# def greet():
#     print("hi")


# greet()
# greet()

"""
Code this decorator.

@require_positive
def square(x):

    return x * x
"""


# def require_positive(func: Callable):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         if any(x < 0 for x in args):
#             raise ValueError("negative numbers not allowed.")
#         result = func(*args, **kwargs)
#         return result

#     return wrapper


# @require_positive
# def square(x):
#     return x * x


# print(square(-2))


"""
Time taken by a coroutine.

@async_timed()

async def fetch():
    await asyncio.sleep(1)
"""


def async_timed():
    def wrapped(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            print(f"{func.__name__} started with args {args} {kwargs}")
            start = time.time()
            result = await func(*args, **kwargs)
            end = time.time()
            total = end - start
            print(f"Time taken: {total} secs")
            return result

        return wrapper

    return wrapped
