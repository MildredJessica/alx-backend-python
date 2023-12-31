#!/usr/bin/env python3

"""Measure the runtime"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for and returns a float"""
    start = time.perf_counter()
    await asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
