class User:
    _users = [
        {"username": "admin", "password": "admin123", "role": "admin"},
        {"username": "maqueiro", "password": "maqueiro123", "role": "maqueiro"}
    ]

    def __init__(self, username, role):
        self.username = username
        self.role = role

    @classmethod
    def authenticate(cls, username, password):
        for user in cls._users:
            if user["username"] == username and user["password"] == password:
                return User(username, user["role"])
        return None
