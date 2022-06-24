class UserAddress:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {} .".format(
            guest_name, self.name, self.email))


user1 = UserAddress('jane', 'Jane Doe', 'jane@doe.com')

print("User Object address on the disk is printed", user1)


# calling the class methods
user1.introduce_yourself('David')


class UserString:
    def __init__(self, name,  username, email):
        self.name = name
        self.email = email
        self.username = username
    print("User created")

    """
    __repr__ and __str__ are used to create a string representation on the object.
    """

    def __repr__(self):
        return "User(username='{}',name='{}',email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()


user2 = UserString("vivek", "fifa", "vivek@fifa.com")

print("String representation of the user is printed", user2)
