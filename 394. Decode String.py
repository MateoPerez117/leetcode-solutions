# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

s = "3[a]2[bc]"
stack = []
strstack = []
numstack = []

for i in range  (len(s)):
    if s[i] in "abcdefghijklmnopqrstuvwxyz":
        stack.append(s[i])
    if s[i] in "123456789":
        while s[i] in "123456789":
            numstack.append(s[i])
            i += 1
        numero = int("".join(numstack))

    if s[i] == "[":
        i += 1
        while s[i] != "]":
            strstack.append(s[i])
            i += 1
        i += 1

        string = "".join(strstack)

        for i in range (numero -1):
            stack.append(string)
            print (stack)
        
        numstack.clear()
        numero = 0
        string = ""
        strstack.clear()

print (stack)
output = "".join(stack)

print (output)
