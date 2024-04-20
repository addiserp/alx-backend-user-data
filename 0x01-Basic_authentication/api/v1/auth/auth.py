#!/usr/bin/env python3
"""
A class module of an authentication
"""
from flask import request


class Auth:
    """
    A class for managing the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        if endpoint requires auth this method will validat
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

    def authorization_header(self, request=None) -> str:
        """
        the method authorization header for handling authorization
        """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        It checks the current user
        """
        return None
