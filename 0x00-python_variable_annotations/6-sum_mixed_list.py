#!/usr/bin/env python3

"""6. Complex types - mixed list"""

from typing import Union


def sum_mixed_list(mxd_lst: list[Union[float, int]]) -> float:
    """return the sum of the list"""
    return sum(mxd_lst)