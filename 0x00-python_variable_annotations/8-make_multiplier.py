#!/usr/bin/env python3
"""
8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float 
    """
    def _float(n: float) -> float:
        """
        returns a function that multiplies a float 
        """
        return float(n * multiplier)
    return _float
