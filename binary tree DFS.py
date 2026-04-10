class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

def contar(node):

    if not node:
        return 0

    izquierda = contar(node.left)
    derecha = contar(node.right)

    return 1 + izquierda + derecha

a = contar(root)

print(a)