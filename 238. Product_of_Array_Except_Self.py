nums = [1,2,3,4]

n = len(nums)

left = [1] * n
right = [1] * n
ans = [1] * n

uno = 1
for i in range(n):
    left[i] = uno
    uno *= nums[i]

uno = 1
for i in range(n -1, -1, -1):
    right[i] = uno
    uno *= nums[i]

for i in range(n):
    ans[i] = left[i] * right[i]

print(ans)







