s = "abc" 
t = "ahbgdc"

i = 0
j = 0 

while i != len(t) and j != len(s):
    if s[j] == t[i]:
        j += 1
    if i != (len(t)):
        i += 1

if j == len(s):
    print (True)
        
else:
    print (False)
