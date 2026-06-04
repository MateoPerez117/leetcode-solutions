class TreeNode:
    def __init__(self, val= 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(4)

flag = True

def dfs(node1, node2):
    global flag

    if not node1 and not node2:
        return 
    if not node1 or not node2:
        flag = False
    
    if node1.val != node2.val:
        flag = False
    
    dfs(node1.left, node2.left)
    dfs(node1.right, node2.right)

    return flag

a = dfs(p,q)

print (a)