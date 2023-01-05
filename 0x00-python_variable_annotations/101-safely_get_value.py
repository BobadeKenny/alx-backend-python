#!/usr/bin/env python3

"""101. Basic annotations - safely get value"""


from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar('T'),
                     None] = None) -> Union[Any, TypeVar('T')]:
    """return the value of a key in a dict"""
    if key in dct:
        return dct[key]
    else:
        return default
