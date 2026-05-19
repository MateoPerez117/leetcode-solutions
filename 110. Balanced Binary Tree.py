

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        val.self = val
        left.self = left
        right.self = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

flag = True

def height(node):

    if not node:
        return 0
    
    izquierda = height(node.left)
    derecha = height(node.right)

    if abs(izquierda - derecha) > 1:
        flag = False
    
    return 1 + max(izquierda, derecha)

a = height(root)

print (a)
    
