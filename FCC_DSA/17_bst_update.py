# QUESTION : Write a function to update the value associated with a given key within a BST
def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value


update(tree, 'hemanth', User('hemanth', 'Hemanth J', 'hemanthj@example.com'))

node = find(tree, 'hemanth')
print(node.value)
