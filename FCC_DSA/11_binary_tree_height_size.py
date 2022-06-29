tree = parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))


def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


tree_height(tree)


def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)


tree_size(tree)
