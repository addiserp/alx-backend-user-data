#!/usr/bin/env python3
"""
    function that expects one string argument name password and returns
    a salted, hashed password, which is a byte string.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
        returns a salted, hashed password, which is a byte string.
    """
    bpass = b'password'
    hashed = bcrypt.hashpw(bpass, bcrypt.gensalt())
    return hashed

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
        function that expects 2 arguments and returns a boolean.    
    """
    if bcrypt.checkpw(b'password', hashed_password):
        return True
    else:
        return False
