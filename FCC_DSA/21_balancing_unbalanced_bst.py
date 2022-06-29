# QUESTION: Write a function to balance an unbalanced binary search tree.
def balance_bst(node):
    return make_balanced_bst(list_all(node))


tree1 = None

for user in users:
    tree1 = insert(tree1, user.username, user)

display_keys(tree1)

tree2 = balance_bst(tree1)

display_keys(tree2)
