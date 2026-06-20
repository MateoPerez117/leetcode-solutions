from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)



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

#patrón mental bfs

# queue = deque([root])

# while queue:
#     node = queue.popleft()

#     # proceso el nodo

#     if node.left:
#         queue.append(node.left)

#     if node.right:
#         queue.append(node.right)