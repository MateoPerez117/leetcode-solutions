# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000

nums = [9,7,3,5,6,2,0,8,1,9]
k = 6
slwindow = sum(nums[:k])
maxoutput = float('-inf')
output = slwindow / k

for i in range (k, len(nums)):
    maxoutput = max(output, maxoutput)
    print (output)
    slwindow = slwindow - nums[i - k] + nums[i]
    output = slwindow / k

maxoutput = max(output, maxoutput)
print (maxoutput)