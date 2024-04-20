#!/usr/bin/env python3
"""
A class module of an authentication
"""
from flask import request
from typing import List, TypeVar


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

        l_path = len(path)
        if l_path == 0:
            return True

        slash_path = True if path[l_path - 1] == '/' else False

        tmp_path = path
        if not slash_path:
            tmp_path += '/'

        for exc in excluded_paths:
            l_exc = len(exc)
            if l_exc == 0:
                continue

            if exc[l_exc - 1] != '*':
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[:l_exc - 1]:
                    return False

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


def session_cookie(self, request=None):
    """Returns a cookie from a given request
        Args:
            request : request object
        Return:
            value of _my_session_id cookie from request object
    """
    if request is None:
        return None
    session_name = os.getenv('SESSION_NAME')
    return request.cookies.get(session_name)
