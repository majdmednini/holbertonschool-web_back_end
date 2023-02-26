#!/usr/bin/python3
"""
0. Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    no limit
    """
    def put(self, key, item):
        """
        random comment
        """
        if not key or not item:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        random comment
        """
        if not key or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
