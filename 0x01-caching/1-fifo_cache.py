#!/usr/bin/env python3
"""
This module contains the FIFOCache class
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A caching system
    """
    def __init__(self):
        """
        Calls the parent init and instantiate the self.keys list
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.keys.append(key)

            if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
                key = self.keys[0]
                del self.cache_data[key]
                self.keys.pop(0)
                print('DISCARD: {}'.format(key))

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key)
