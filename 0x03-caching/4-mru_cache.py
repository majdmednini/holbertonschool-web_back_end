#!/usr/bin/python3
"""
4. MRU Caching
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class
    """
    AGE = 0
    AGE_BITS = {}

    def __init__(self):
        """
        random comment
        """
        super().__init__()

    def put(self, key, item):
        """
        random comment
        """
        if key is None or item is None:
            return
        if (len(self.cache_data.items()) == BaseCaching.MAX_ITEMS):
            if (key not in self.cache_data.keys()):
                MostuItem = {
                    k: v for k, v in sorted(self.AGE_BITS.items(),
                                            key=lambda item: item[1])
                }
                MostuItem = list(MostuItem)[-1]
                print("DISCARD:", MostuItem)
                self.cache_data.pop(MostuItem)
                self.AGE_BITS.pop(MostuItem)

        self.cache_data[key] = item
        self.AGE += 1
        self.AGE_BITS[key] = self.AGE

    def get(self, key):
        """
        random comment
        """
        if key not in self.cache_data.keys():
            return None
        else:
            self.AGE += 1
            self.AGE_BITS[key] = self.AGE
            return self.cache_data[key]
