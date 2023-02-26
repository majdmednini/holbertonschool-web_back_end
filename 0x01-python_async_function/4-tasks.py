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
    L = []
    tasks = [task_wait_random(max_delay) for x in range(n)]
    for t in asyncio.as_completed(tasks):
        L.append(await t)
    L.sort()
    return L
