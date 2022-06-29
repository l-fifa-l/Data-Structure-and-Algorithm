'''QUESTION 1: As a senior backend engineer at Jovian, you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email) for 100 million users. It should allow the following operations to be performed efficiently:

Insert the profile information for a new user.
Find the profile information of a user, given their username
Update the profile information of a user, given their usrname
List all the users of the platform, sorted by username
You can assume that usernames are unique.

We can create a generic class TreeMap which supports all the operations specified in the original problem statement in a python-friendly manner.'''


class TreeMap():
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)

    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in list_all(self.root))

    def __len__(self):
        return tree_size(self.root)

    def display(self):
        return display_keys(self.root)


print(users)

treemap = TreeMap()

treemap.display()

treemap['aakash'] = aakash
treemap['jadhesh'] = jadhesh
treemap['sonaksh'] = sonaksh

treemap.display()

treemap['jadhesh']

len(treemap)

treemap['biraj'] = biraj
treemap['hemanth'] = hemanth
treemap['siddhant'] = siddhant
treemap['vishal'] = vishal

treemap.display()

for key, value in treemap:
    print(key, value)

list(treemap)


treemap['aakash'] = User(
    username='aakash', name='Aakash N S', email='aakashns@example.com')

treemap['aakash']
