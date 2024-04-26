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


def _generate_uuid() -> str:
    """
    will return a string representation of a new UUID
    """
    UUID = uuid4()
    return str(UUID)


class Auth:
    """
    the authentication database to interact with user.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        this will registers a user in the database
        Returns: User Object
        """

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)

            return user

        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """
        this will check If password is valid returns true, else, false
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        user_password = user.hashed_password
        encoded_password = password.encode()

        if bcrypt.checkpw(encoded_password, user_password):
            return True

        return False

    def create_session(self, email: str) -> str:
        """
        this will returns session ID for a user
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()

        self._db.update_user(user.id, session_id=session_id)

        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """
        this will take a single session_id string argument
        Returns a string or None
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return user

    def destroy_session(self, user_id: int) -> None:
        """
        this will update the corresponding user's session ID to None
        """
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None

        self._db.update_user(user.id, session_id=None)

        return None

    def get_reset_password_token(self, email: str) -> str:
        """
        this will generates a reset password token if user exists
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        reset_token = _generate_uuid()

        self._db.update_user(user.id, reset_token=reset_token)

        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """
        this will use a reset token to validate update of users password
        """
        if reset_token is None or password is None:
            return None

        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        hashed_password = _hash_password(password)
        self._db.update_user(user.id,
                             hashed_password=hashed_password,
                             reset_token=None)
