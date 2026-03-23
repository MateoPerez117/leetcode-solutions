# Input: nums = [1,3,5,6], target = 5
# Output: 2

nums = [1,3,5,6]
target = 7
flag = True
i = 0

while flag:
    if i == len(nums):
        break
    if nums[i] == target:
        break
    if nums[i] > target:
        break
    i += 1

print(i)    