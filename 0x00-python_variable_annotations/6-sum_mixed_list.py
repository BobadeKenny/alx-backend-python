#!/usr/bin/env python3

"""6. Complex types - mixed list"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of the list"""
    return sum(mxd_lst)
