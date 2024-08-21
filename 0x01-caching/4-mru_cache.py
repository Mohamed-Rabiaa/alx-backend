#!/usr/bin/env python3
"""
This module contains the MRUCache class
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
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
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed_key = self.keys.pop(-1)
                del self.cache_data[removed_key]
                print('DISCARD: {}'.format(removed_key))

            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key)
