#!/usr/bin/env python3
""" Authentication
"""
from typing import List, TypeVar
from flask import request


class Auth():
    """ Class Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ method require_auth
        """
        if path is None:
            return True
        if not excluded_paths or excluded_paths is None:
            return True
        if path[-1] != '/':
            path += '/'

        for paths in excluded_paths:
            if paths.endswith('*'):
                if path.startswith(paths[:-1]):
                    return False
            elif path == paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ method authorization_header
        """
        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ method current_user
        """
        return None
