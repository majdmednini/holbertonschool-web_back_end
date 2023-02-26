#!/usr/bin/env python3
"""
5. Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    returns their sum as a float
    """
    sum = 0
    for i in input_list:
        sum += i
    return sum
