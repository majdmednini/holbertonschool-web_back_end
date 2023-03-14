#!/usr/bin/env python3
"""
9. Insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """
    ins docs
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
