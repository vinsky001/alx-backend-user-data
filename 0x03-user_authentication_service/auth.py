#!/usr/bin/env python3
"""
Authentication module
"""

import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """Hash the password using the bcrypt module"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user"""
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            user = None
        if user:
            raise ValueError('User {} already exist'.format(email))
        hashed_password = _hash_password(password)
        return self._db.add_user(email, hashed_password)