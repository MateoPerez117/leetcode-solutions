class TreeNode:
    def __init__(self, val, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left


root = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)


root.left = b
root.right = c
c.left = d
c.right = e


def max_depth(self, root):
    if not root:
        return 0
           
    return 1 + max(
        self.maxDepth(root.left),
        self.maxDepth(root.right)
            )


a = max_depth(root, root )


print (a)
