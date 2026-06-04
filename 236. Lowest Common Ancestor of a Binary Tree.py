class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p = 5
q = 1

root = TreeNode(3)

root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

def dfs(node, p, q):

    if not node:
        return
    
    if node.val == p or node.val == q:
        return node
    
    left = dfs(node.left, p, q)
    right = dfs(node.right, p, q)

    if left and right:
        return node
    
    if left or right:
        return left or right
    
    return None

answer = dfs(root, p, q)
print(answer.val)