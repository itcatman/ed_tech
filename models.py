class User():
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def get_json(self):
        data = {
            'name': self.name,
            'password': self.password,
        }
        return data


