#!/usr/bin/env python3

"""8. Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a function that multiplies a float by multiplier"""
    def multiply(n: float) -> float:
        """return the product of n and multiplier"""
        return n * multiplier
    return multiply
