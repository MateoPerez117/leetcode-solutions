asteroids = [5, 10, -5]
stack = []

for a in asteroids:
    if a > 0:
        stack.append(a)
    else:
        num = abs(a)

        while stack and stack[-1] > 0 and num > stack[-1]:
            stack.pop()

        if not stack or stack[-1] < 0:
            stack.append(a)

        elif num == stack[-1]:
            stack.pop()

print(stack)
