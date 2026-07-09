'''
class Sessionservice:
    def __init__(self):
        self.sessions = {}

    def save_state(
        self,
        session_id : str,
        state : dict):
        self.sessions[session_id] = state

    def get_state(self, session_id: str):
        return self.sessions.get(session_id)

    def delete_state(self, session_id : str):
        self.sessions.pop(session_id, None)


session_service = Sessionservice()'''


from copy import deepcopy


class SessionService:

    def __init__(self):
        self.sessions = {}

    def save_state(self, session_id, state):
        self.sessions[session_id] = deepcopy(state)

    def get_state(self, session_id):
        state = self.sessions.get(session_id)

        if state:
            return deepcopy(state)

        return None

    def delete_state(self, session_id):
        self.sessions.pop(session_id, None)


session_service = SessionService()