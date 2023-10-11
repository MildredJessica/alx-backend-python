#!/usr/bin/env python3

"""Execute multiple coroutines at the same time with async"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Return the list of all the delays and sorts in ascending order"""
    new_list = await asyncio.gather(
            *(wait_random(max_delay) for _ in range(n)))
    return sorted(new_list)
