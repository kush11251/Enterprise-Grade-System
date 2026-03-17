from models import User
from adapters.user_adapter import UserAdapter

class UserRepository:
    def __init__(self):
        self.user_adapter = UserAdapter()

    def get_users(self):
        return self.user_adapter.get_users()