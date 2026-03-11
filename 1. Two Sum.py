# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

nums = [8,2,11,7,15]
target = 9
need = 0
dic = {}

for i in range(len(nums)):
    dic[nums[i]] = i

for i in range(len(nums)):
    need = target - nums[i]

    if need in dic and dic[need] != i:
        print (dic[need], i)
        break

print (dic)
                
