#!/usr/bin/env python3

"""Let's duck type an iterable object"""

from typing import Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate the function’s parameters
    return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
