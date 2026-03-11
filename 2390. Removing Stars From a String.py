s = "leet**cod*e"
stack = []

for i in range (len(s)):
    if s[i] != "*":
        stack.append(s[i])
    else:
        stack.pop()

stack = "".join(stack)
print (stack)
#########################
#una mejor forma de hacerlo papu
s = "leet**cod*e"
stack = []

for char in s:
    if char != "*":
        stack.append(char)
    else:
        stack.pop()

print ( "".join(stack))