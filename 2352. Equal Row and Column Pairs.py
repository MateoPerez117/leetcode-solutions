# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1

grid = [[3,1,2,2],
        [1,4,4,4],
        [2,4,2,2],
        [2,5,2,2]
]
columns = []
n = 0

for j in range (len (grid)):
    c = []
    for i in range (len(grid)):
        c.append(grid[i][j])
    columns.append(c)

for i in range(len(grid)):
    n += columns.count(grid[i])

print (n)