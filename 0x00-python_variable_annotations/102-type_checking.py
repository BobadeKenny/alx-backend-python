#!/usr/bin/env python3

"""102. Type Checking"""

from typing import Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """zoom_array"""
    zoomed_in: Tuple = (
        lst[0] / factor,
        lst[1] / factor,
        lst[2] * factor,
        lst[3] * factor
    )
    return zoomed_in
