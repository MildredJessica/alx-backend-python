#!/usr/bin/env python3

"""New function task_wait_n"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """The code is nearly identical to wait_n except task_wait_random"""
    new_list = await asyncio.gather(
                           *(task_wait_random(max_delay) for _ in range(n)))
    return sorted(new_list)
