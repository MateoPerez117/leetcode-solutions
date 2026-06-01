nums = [1,2,3,1]
seen = set()
flag = False

for i in range (len(nums)):
    if nums[i] in seen:
        flag = True
    else:
        seen.add(nums[i])

print ( flag ) 

# esta fue mi solucion, pero esta esta mucho mucho mejor

nums = [1,2,3,1]
sett = nums(set)

if len(sett) == len(nums):
    print (False)
else:
    print(True)