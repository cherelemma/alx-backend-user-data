#!/usr/bin/env python3
"""
class for a User session
"""
from models.base import Base


class UserSession(Base):
    """
    contains methods that manages a user's session and session ids
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
  
