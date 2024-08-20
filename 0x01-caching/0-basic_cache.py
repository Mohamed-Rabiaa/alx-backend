#!/usr/bin/env python3
"""
This module contains the BasicCache class
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A caching system
    """
    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key)
