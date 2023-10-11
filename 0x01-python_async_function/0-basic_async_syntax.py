#!/usr/bin/env python3

""" The basics of async """

import asyncio
from random import uniform as ru


async def wait_random(max_delay=10):
    """Asynchronous coroutine that takes in an integer argument"""
    num = ru(0, max_delay)
    await asyncio.sleep(num)
    return num
