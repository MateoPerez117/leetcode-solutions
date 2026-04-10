class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root1 = TreeNode(3)

n5 = TreeNode(5)
n1 = TreeNode(1)

n6 = TreeNode(6)
n2 = TreeNode(2)

n9 = TreeNode(9)
n8 = TreeNode(8)

n7 = TreeNode(7)
n4 = TreeNode(4)

root1.left = n5
root1.right = n1

n5.left = n6
n5.right = n2

n2.left = n7
n2.right = n4

n1.left = n9
n1.right = n8

root2 = TreeNode(3)

m5 = TreeNode(5)
m1 = TreeNode(1)

m6 = TreeNode(6)
m7 = TreeNode(7)

m4 = TreeNode(4)
m2 = TreeNode(2)

m9 = TreeNode(9)
m8 = TreeNode(8)

root2.left = m5
root2.right = m1

m5.left = m6
m5.right = m7

m1.left = m4
m1.right = m2

m2.left = m9
m2.right = m8


class Solution:
    def leafSimilar(self, root1, root2):
        leafs1 = []
        leafs2 = []

        def dfs(node, leafs):

            if not node:
                return

            if not node.left and not node.right:
                leafs.append(node.val)
                return
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root1, leafs1)
        dfs(root2, leafs2)

        return leafs1 == leafs2