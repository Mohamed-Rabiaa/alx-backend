#!/usr/bin/env python3
"""
This module contains the LIFOCache class
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
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
            if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    k = self.keys[-1]
                    del self.cache_data[k]
                    self.keys.pop()
                    print('DISCARD: {}'.format(k))

            self.cache_data[key] = item
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key)
