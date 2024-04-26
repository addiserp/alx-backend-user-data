#!/usr/bin/env python3
"""
    a _hash_password method that takes in a password
    string arguments and returns bytes.
"""

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
from user import User
from uuid import uuid4


def _hash_password(password: str) -> str:
    """
    a _hash_password method that takes in
    a password string arguments and returns bytes.
    """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed
