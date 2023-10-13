#!/usr/bin/env python3

"""Async Generator"""

import asyncio
from random import uniform as ru


async def async_generator():
    """Coroutine will loop 10 times yield a random number between 0 and 10"""
    await asyncio.sleep(1)
    for _ in range(10):
        yield ru(0, 10)
