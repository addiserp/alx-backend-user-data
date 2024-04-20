#!/usr/bin/env python3
"""
A class module of an authentication
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    A class for managing the Basic API authentication
    """
