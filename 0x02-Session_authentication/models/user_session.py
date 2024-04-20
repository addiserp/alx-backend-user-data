#!/usr/bin/env python3
"""
UserSession module inherits from base
"""
from models.base import Base


class UserSession(Base):
    """ UserSession class from base model"""

    def __init__(self, *args: list, **kwargs: dict):
        """ this will Initialize a UserSession instance """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
