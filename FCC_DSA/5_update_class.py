class User:
    def __init__(self, name, email, username):
        self.name = name
        self.email = email
        self.username = username
    print("User created")

    def introduce_youself(self, guestname):
        print(f"Hi {guestname} I'm {self.name}! contact me at {self.email}")


user1 = User("John", "jo@neja.com", "janeja")

print(user1.name)

user1.introduce_youself("David")
