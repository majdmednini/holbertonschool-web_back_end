#!/usr/bin/env python3
"""
4. Tasks
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    return list
    """
    L = await asyncio.gather(*[task_wait_random(max_delay) for y in range(n)])
    return sorted(L)
