from models import User

class UserAdapter:
    def get_users(self):
        # Mock data for demonstration purposes
        return [User(id=1, name='John Doe', email='john@example.com')]