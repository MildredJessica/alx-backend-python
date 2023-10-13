#!/usr/bin/env python3

""" Async Comprehensions"""

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Collects 10 random numbers from async_generator, returns the numbers."""
    return [i async for i in async_generator()]
