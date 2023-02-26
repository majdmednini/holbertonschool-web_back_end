#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""

from typing import List

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns the 10 random numbers
    """
    ord = [wait_random(max_delay) for x in range(n)]
    l = []
    for i in asyncio.as_completed(ord):
        r = await i
        l.append(r)
    return(l)
