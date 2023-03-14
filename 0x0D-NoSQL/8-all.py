#!/usr/bin/env python3
"""
8. List all documents in Python
"""


def list_all(mongo_collection):
    """
    listing all docs
    """
    return mongo_collection.find() or []
