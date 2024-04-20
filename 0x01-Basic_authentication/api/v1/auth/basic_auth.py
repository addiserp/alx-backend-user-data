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
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
            A mothod for exctracting to base64
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        encoded = authorization_header.split(' ', 1)[1]

        return encoded
