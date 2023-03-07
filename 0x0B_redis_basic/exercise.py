#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""
import redis
import sys
from typing import Callable, Optional, Union
import uuid


class Cache():
    """
    cache class
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method
        """
        random_id = str(uuid.uuid4())
        self._redis.set(random_id, data)
        return random_id

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        get method
        """
        return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_str(self, value: bytes) -> str:
        """
        str method
        """
        return value.decode("utf-8")

    def get_int(self, value: bytes) -> str:
        """
        int method
        """
        return int.from_bytes(value, sys.byteorder)
