#!/usr/bin/env python3

"""Async Generator"""

import asyncio
from random import uniform as ru


async def async_generator():
    await asyncio.sleep(1)
    for _ in range(10):
        yield ru(0, 10)
    