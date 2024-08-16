#!/usr/bin/env python3
"""
This module contains the index_range function
"""

import csv
import math
from typing import Tuple, List, Dict


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
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0
        start, end = self.index_range(page, page_size)
        dataset = self.dataset()
        dataset_len = len(dataset)
        if start > dataset_len or end > dataset_len:
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        get_hyper function
        """
        data = self.get_page(page, page_size)
        original_dataset = self.dataset()
        dct = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': page + 1 if len(data) > 0 else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': math.ceil(len(original_dataset) / page_size)
        }
        return dct

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
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
