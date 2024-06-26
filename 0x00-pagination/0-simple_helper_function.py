#!/usr/bin/env python3
"""
Defining a function named `index_range`
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculating start index and an end index corresponding to the range of
    indexing to return in a list for those particular pagination parameters.
    Args:
        page (int): the current page
        page_size (int): the amount of items in a page
    Returns:
        tuple of the start and end index for the given page
    """
    nextPageStartIndex = page * page_size
    return nextPageStartIndex - page_size, nextPageStartIndex
