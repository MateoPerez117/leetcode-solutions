class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)




root.left = b
root.right = c
c.left = d
c.right = e


def max_depth(root):


    current = root
    contador = 0
    maxcontador = 0


    while current:
        contador += 1
        current.left = current