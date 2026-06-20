class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(989)

root.right = TreeNode(10250)

root.right.left = TreeNode(98693)
root.right.right = TreeNode(-89388)

root.right.right.right = TreeNode(-32127)

from collections import deque

def bfs(node):
    
    if not node:
        return 0
    
    queue = deque([root])
    level_len = len(queue)
    maximo = float('-inf')
    total_sum = 0
    contador =0

    while queue:
        contador += 1

        level_len = len(queue)

        for i in range(level_len):

            node = queue.popleft()
            total_sum += node.val

            if node.left:
                queue.append(node.left)
        
            if node.right:
                queue.append(node.right)
        
        if total_sum > maximo:
            winner = contador

        maximo = max(total_sum, maximo)
        total_sum = 0
    
    return winner
        
a = bfs(root)

print (a)