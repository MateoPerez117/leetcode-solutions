class TreeNode:
    def __init__(self, val=0, left =None, right=None):
        self.val = val
        self.right = right
        self.left = left

root = TreeNode(1)

a = TreeNode(2)
b = TreeNode(3) 
c = TreeNode(4)
d = TreeNode(5)

root.left = a
root.right = b

a.left = c
a.right = d

def dfs_preorder(node):

    if not node:
        return

    print(node.val)

    dfs_preorder(node.left)

    dfs_preorder(node.right)

print(dfs_preorder(root))