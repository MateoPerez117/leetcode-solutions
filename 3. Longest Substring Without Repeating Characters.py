# Input: s = "abcabcbb"
# Output: 3


s = "bbbbb"
hasht = []
cont = 0
maxsub = 0

for i in range (len(s)):
    if s[i] not in hasht:
        hasht.append(s[i])
        cont += 1
    else:
        while s[i] in hasht:    
            maxsub = max(maxsub, cont)
            cont -= 1
            hasht.pop(0)
        hasht.append(s[i])
        cont += 1

maxsub = max(maxsub, cont)

print (maxsub)
