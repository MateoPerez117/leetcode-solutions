class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Nivel 0
root = TreeNode(10)

# Nivel 1
n5 = TreeNode(5)

n_3 = TreeNode(-3)

root.left = n5
root.right = n_3

n3_left = TreeNode(3)
n2 = TreeNode(2)

n5.left = n3_left
n5.right = n2

n3_leaf = TreeNode(3)
n_2 = TreeNode(-2)

n3_left.left = n3_leaf
n3_left.right = n_2

n1 = TreeNode(1)

n2.right = n1

n11 = TreeNode(11)

n_3.right = n11

targetSum = 8

def count_from(node, suma):
    
    if not node:
        return 0
    
    suma += node.val
    
    count = 0
    
    if suma == targetSum:
        count = 1
    
    count += count_from(node.left, suma)
    count += count_from(node.right, suma)
    
    return count

def dfs(node):

    if not node:
        return 0
    
    total = count_from(node, 0)

    total += dfs(node.left)
    total += dfs(node.right)

    return total

print( dfs(root))
