# QUESTION : Write a function to retrieve all the key-values pairs stored in a BST in the sorted order of keys.

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)


list_all(tree)
