
#!/usr/bin/env python3
"""
0x05. Personal data
"""
import bcrypt

def hash_password(password: str) -> bytes:
    """
    a function that expects one string argument
    """
    password = bytes(password, 'utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    a function that expects 2 arguments and returns a boolean
    """
    if bcrypt.checkpw(bytes(password, 'utf-8'), hashed_password):
        return True
    else:
        return False