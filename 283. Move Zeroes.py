nums = [0,1,0,0,0,0,0]
longitud = len(nums) -1
j = 1
i = 0

if longitud == 0:
    i = 1
else:
    while i != longitud - 1:
        if nums[j] == 0:
            x = nums.pop(j) 
            nums.append(x)

        elif nums[i] == 0:
            x = nums.pop(0) 
            nums.append(x)
            j += 1
            i +=1

print(nums)
