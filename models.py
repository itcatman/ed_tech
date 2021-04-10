class User():
    def __init__(self, name, password, birthday, school_class, role):
        self.name = name
        self.password = password
        self.birthday = birthday
        self.school_class = school_class
        self.role = role

    def __str__(self):
        return 'Name: {0}\nPassword: {1}\nBirthday: {2}\nClass: {3}\nRole: {4}'.format(
            self.name,
            self.password,
            self.birthday,
            self.school_class,
            self.role
        )

