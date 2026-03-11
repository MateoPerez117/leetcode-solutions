nums = [20,100,10,12,5,13]
first = float("inf")
second = float("inf")
flag = False

for i in nums:
    if i <= first:
        first = i
    elif i < second:
        second = i
    else:
        flag = True
    
print(flag)
