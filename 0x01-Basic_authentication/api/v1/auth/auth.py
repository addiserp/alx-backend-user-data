#!/usr/bin/env python3
""" Class for Auth
"""
from flask import request


class Auth:
    """
        A class simple API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            A method that handles require auth
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

    def authorization_header(self, request=None) -> str:
        """
            A method that handles authorization header
        """
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            It validates current user
        """
        return None
