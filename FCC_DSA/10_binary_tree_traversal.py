"""
QUESTION 1: Write a function to perform the inorder traversal of a binary tree.

QUESTION 2: Write a function to perform the preorder traversal of a binary tree.

QUESTION 3: Write a function to perform the postorder traversal of a binary tree.

"""
# ? Inorder


def traverse_in_order(node):
    if node is None:
        return []
    return(traverse_in_order(node.left) +
           [node.key] +
           traverse_in_order(node.right))


tree = parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))

display_keys(tree, '  ')

traverse_in_order(tree)
