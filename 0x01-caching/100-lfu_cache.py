#!/usr/bin/env python3
"""
This module contains the LFUCache class
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    A caching system
    """
    def __init__(self):
        """
        Calls the parent init and instantiate the self.keys list
        """
        super().__init__()
        self.frequency = {}
        self.ordered_keys = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1

            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    min_freq = min(self.frequency.values())
                    lfu_keys = [k for k, v in self.frequency.items()
                                if v == min_freq]

                    if len(lfu_keys) > 1:
                        for k in self.ordered_keys:
                            if k in lfu_keys:
                                discard_key = k
                                break
                    else:
                        discard_key = lfu_keys[0]

                    del self.cache_data[discard_key]
                    del self.frequency[discard_key]
                    self.ordered_keys.remove(discard_key)
                    print('DISCARD: {}'.format(discard_key))

                self.cache_data[key] = item
                self.frequency[key] = 1

            if key in self.ordered_keys:
                self.ordered_keys.remove(key)
            self.ordered_keys.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key in self.cache_data:
            self.frequency[key] += 1
            self.ordered_keys.remove(key)
            self.ordered_keys.append(key)
        return self.cache_data.get(key)
