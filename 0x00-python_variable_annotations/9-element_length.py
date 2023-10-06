#!/usr/bin/env python3

"""Let's duck type an iterable object"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: List[Iterable[Sequence]]) -> Tuple[Sequence]:
    """Annotate the function’s parameters
    return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
