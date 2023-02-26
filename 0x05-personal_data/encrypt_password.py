#!/usr/bin/env python3
"""
0x05. Personal data
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    a function that expects one string argument
    """
    binary_password = bytes(password, "ascii")
    return bcrypt.hashpw(binary_password, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    a function that expects 2 arguments and returns a boolean
    """
    return bcrypt.checkpw(bytes(password, "ascii"), hashed_password)
