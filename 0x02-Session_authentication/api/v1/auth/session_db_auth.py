#!/usr/bin/env python3
"""
create a new authentication system, based on Session ID stored in database
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    contains methods that handles creating
    a new authentication system, based on Session ID stored in database
    """

    def create_session(self, user_id=None):
        """
        creates a session id and saves to a file
        """
        self.session_id = super().create_session(user_id)
        if not self.session_id:
            return None
        user_session_inf = {'session_id': self.session_id, 'user_id': user_id}
        user_session = UserSession(**user_session_inf)
        user_session.save()
        return self.session_id

    def user_id_for_session_id(self, session_id=None):
        """
        returns the User ID by requesting UserSession in the
        database based on session_id
        """

        if not session_id:
            return None

        UserSession.load_from_file()
        sessions = UserSession.search({'session_id': session_id})

        if not sessions:
            return None

        for session in sessions:
            return session.user_id
        return None

    def destroy_session(self, request=None):
        """
        destroys the UserSession based on the Session ID from the request
        cookie
        """
        if not request:
            return False
        self.session_id = self.session_cookie(request)
        if not self.session_id:
            return False
        UserSession.load_from_file()
        sessions_present = UserSession.search({'session_id': self.session_id})
        if not sessions_present:
            return False
        for session in sessions_present:
            del session
            return True
        return False
    
