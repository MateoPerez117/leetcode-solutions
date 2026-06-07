g = [1,2,3]
s = [1,1]

g = sorted(g)
s = sorted(s)

i = 0
j = 0
output = 0

while i< len(g) and j < len(s):

    if g[i] <= s[j]:
        output += 1
        j += 1
        i += 1
    else:
        j += 1

print (output)