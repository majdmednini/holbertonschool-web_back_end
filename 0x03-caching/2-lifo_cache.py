#!/usr/bin/env python3
"""
2. LIFO Caching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ caching system """

    def __init__(self):
        """
        random comment
        """
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """
        Add item
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_key))
                self.cache_data.pop(self.last_key)
            self.last_key = key

    def get(self, key):
        """
        Return the value
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value
