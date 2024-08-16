#!/usr/bin/env python3
"""
This module contains the index_range function
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters.

    Args:
        page (int): page number
        page_size (int): the number of elements to be displayed in a page

    Returns:
        Tuple[int, int]: a tuple containing the start and end indexes
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
