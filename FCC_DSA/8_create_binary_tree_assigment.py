class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


'''
1) create a tree

       2
     /  \
    3    5
   /   /   \
  1   3      7
      \    /   \
       4  6     8

'''

print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
# 2) create a tree with tuple

# tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))


def parse_tuple(data):
    print(data)
    # checks if data is the type tuple
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


tree2 = parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(tree2)


print(tree2.key)
print(tree2.left.key, tree2.right.key)
print(tree2.left.left.key, tree2.left.right,
      tree2.right.left.key, tree2.right.right.key)
print(tree2.right.left.right.key, tree2.right.right.left.key,
      tree2.right.right.right.key)

print("QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")


def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)

    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return

    # If the node is a leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return

    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left, space, level+1)


display_keys(tree2, '  ')
