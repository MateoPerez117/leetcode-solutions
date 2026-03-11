nums = [1,1,2]
left = 0
k = 1

for right in range(1, len(nums)):
    if nums[left] != nums[right]:
        nums[left + 1] = nums[right]
        left += 1
        k += 1

print (k, nums)