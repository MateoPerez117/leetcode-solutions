class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

n7 = TreeNode(1)

n6 = TreeNode(1)
n6.right = n7

n5 = TreeNode(1)
n5.right = n6

n4 = TreeNode(1)

n3 = TreeNode(1)
n3.left = n5
n3.right = n4

n2 = TreeNode(1)

root = TreeNode(1)
root.left = n2
root.right = n3

n1 = TreeNode(1)
n1.right = root

maxi = 0

def dfs(node, direccion_anterior,longitud):
    global maxi

    if not node:
        return 
    
    maxi = max(maxi, longitud)
    
    if direccion_anterior == "left":
        dfs(node.right, "right", longitud + 1)
        
        dfs(node.right, "right", longitud + 1)

    if direccion_anterior == "right":
        dfs(node.left, "left",  1)

        dfs(node.left, "left", 1)
    
    return maxi


a = dfs(root, "left", 0)
b = dfs(root, "right", 0)

print (max(a,b))
