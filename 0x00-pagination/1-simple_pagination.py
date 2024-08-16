#!/usr/bin/env python3
"""
This module contains the index_range function
"""

import csv
import math
from typing import Tuple, List


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        This function returns a page from dataset after finding the correct
        indexes using the index_range function
        """
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        dataset_len = len(dataset)
        if start > dataset_len or end > dataset_len:
            return []
        return dataset[start:end]


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
