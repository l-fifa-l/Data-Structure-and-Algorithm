# QUESTION 1: Find the value associated with a given key in a BST.
def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)


node = find(tree, 'hemanth')

print(node.key, node.value)
