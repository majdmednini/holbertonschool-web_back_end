#!/usr/bin/env python3
"""
9. Insert a document in Python
"""


def list_all(mongo_collection):
    """
    ins docs
    """
    result = mongo_collection.school.find()
    if result:
        return result
    return []
