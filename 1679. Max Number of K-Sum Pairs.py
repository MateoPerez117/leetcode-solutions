nums = [3,1,3,4,3]
k = 6
need = 0
hashtable = {}
output = 0

for i in range (len(nums)):
    if nums[i] in hashtable:
        hashtable[nums[i]] += 1
    else:
        hashtable[nums[i]] = 1

for i in range(len(nums)):
    need = k - nums[i]

    if need in hashtable and nums[i] in hashtable:
        if need != nums[i]:
            if hashtable[need] > 0 and hashtable[nums[i]] > 0:
                hashtable[need] -= 1
                hashtable[nums[i]] -= 1
                output += 1
        else:
            if hashtable[need] >= 2:
                hashtable[need] -= 2
                output += 1

print (output)