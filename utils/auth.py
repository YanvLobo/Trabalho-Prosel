from models.user import User

class Auth:
    def __init__(self):
        self.users = {
            "admin": User("admin", "admin", "Admin"),
            "maqueiro": User("maqueiro", "maqueiro", "Maqueiro"),
        }

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        return None
