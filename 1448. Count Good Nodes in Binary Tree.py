# Input: root = [3,1,4,3,null,1,5]
# Output: 4

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)

root.left = TreeNode(1)
root.right = TreeNode(4)

root.left.left = TreeNode(3)

root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

maximo = float("-inf")

def Count_Node(node, maximo):

    mi_valor = 0

    if not node:
        return 0
    
    if node.val >= maximo:
        mi_valor = 1 
    
    maximo = max(maximo, node.val)
    
    izquierda = Count_Node(node.left, maximo)
    derecha = Count_Node(node.right, maximo)

    return mi_valor + izquierda + derecha

a = Count_Node(root, maximo)

print  (a)
    

