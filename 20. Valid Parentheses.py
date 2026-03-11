s = "(])"
s = list(s)
stack = []
flag = True

for ch in s:
    if ch in "([{":
        stack.append(ch)
        continue

    if not stack:
        flag = False
        break

    top = stack[-1]
    if (top == "(" and ch != ")") or \
       (top == "[" and ch != "]") or \
       (top == "{" and ch != "}"):
        flag = False
        break
    stack.pop()
if stack:
    flag = False

print(flag)