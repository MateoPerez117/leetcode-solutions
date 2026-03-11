s = ["h","e","l","l","o",]
j = -1
h = len(s) / 2

for i in range (round(h)):
    x = s[i]
    s[i] = s[j]
    s[j] = x
    j -= 1

print (s)