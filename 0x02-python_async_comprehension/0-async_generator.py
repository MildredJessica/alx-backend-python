#!/usr/bin/env python3

"""Async Generator"""

import asyncio
from typing import Generator
from random import uniform as ru


async def async_generator() -> Generator[float, None, None]:
    """Coroutine will loop 10 times yield a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield ru(0, 10)
