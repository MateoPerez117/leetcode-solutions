class TreeNode():
    def __init__(self, val=0, left=None,right=None):
        self.right = right
        self.left = left
        self.val = val

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

output = []

def dfs(node):
    global output

    if not node:
        return
    
    dfs(node.left)
    output.append(node.val)

    dfs(node.right)

    return output

dfs(root)