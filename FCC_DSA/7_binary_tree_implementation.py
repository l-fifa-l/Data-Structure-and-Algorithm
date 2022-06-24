class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)

# check type of node
print(node0)

# key of node0
print(node0.key)

node0.left = node1
node0.right = node2

# print(node0.left.key)
# print(node0.right.key)
# print(node0.key)

tree = node0

print("1 - 0 - 2")
print('Key', tree.key)
print('Left child', tree.left.key)
print('Right child', tree.right.key)
