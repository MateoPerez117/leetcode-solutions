height = [1,8,6,2,5,4,8,3,7]

j = 0
i = len(height) - 1
newater = 0

while j < i:
    maxheight = min(height[j],height[i])
    water =  maxheight * (i - j)

    print (water)
    if water > newater:
        newater = water


    if height[j] < height[i]:
        j += 1
    else:
        i -= 1

print (newater)