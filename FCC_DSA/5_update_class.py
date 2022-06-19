class User:
    def __init__(self, name,  username, email):
        self.name = name
        self.email = email
        self.username = username
    print("User created")

    def __repr__(self):
        return "User(username='{}',name='{}',email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()


john = User("John", "jo", "jo@john.com")
jane = User("Jane", "ja", "ja.jane.com")
vivek = User("Vivek", "fifa", "vivek@fifa.com")
vrinda = User("Vrinda", "bindu", "vrinda@bindu.com")
tanvi = User("Tanvi", "tan", "tanvi@tan.com")
kshitij = User("Kshitij", "harsh", "kshitij@harsh.com")
sharad = User("Sharad", "build", "sharad@build.com")

users = [john, jane, vivek, vrinda, tanvi, kshitij, sharad]

print(john.name, john.email, john.username)
print(john)
print(users)


class UserDatabase:
    def insert(self, user):
        pass

    def find(self, username):
        pass

    def update(self, user):
        pass

    def list_all(self):
        pass
