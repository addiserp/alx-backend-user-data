#!/usr/bin/env python3
"""
    function that expects one string argument name password and returns
    a salted, hashed password, which is a byte string.
"""

import bcrypt

def hash_password(password: str) -> str:
    """
        returns a salted, hashed password, which is a byte string.
    """
    bpass =b'password'
    hashed = bcrypt.hashpw(bpass, bcrypt.gensalt())
    return hashed
