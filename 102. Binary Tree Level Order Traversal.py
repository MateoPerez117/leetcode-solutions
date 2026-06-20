from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

from collections import deque

def bfs(node):
    if not node:
        return

    queue = deque([node])
    result = []
    lala = []

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()

            result.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

                
        lala.append(result)
        result = []
                
    return lala

a = bfs(root)

print (a)