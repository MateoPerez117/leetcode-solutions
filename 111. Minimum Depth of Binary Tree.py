class TreeNode ():
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
a = TreeNode(9)
b = TreeNode(20)
c = TreeNode(15)
d = TreeNode(7)

root.left = a
root.right = b
b.left = c
b.right = d


def dfs(node):
    if not node:
        return 0
    
    if not node.left:
        return 1 + dfs(node.right)
    
    if not node.right:
        return 1 + dfs(node.left)
    
    left = dfs(node.left)
    right = dfs(node.right)

    return 1 + min(left,right)

print(dfs(root))