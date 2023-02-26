#!/usr/bin/env python3
"""
2. Measure the runtime
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    returns a float
    """
    start_time = 0.0
    total_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    start_time = time.perf_counter() - total_time
    return total_time / n
