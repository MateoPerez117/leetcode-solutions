candies = [2,3,5,1,3]
extracandies = 3
greatest = 0
result = []
for i in range(len(candies)):
    if candies[i] >= greatest:
        greatest = candies[i]

for i in range(len(candies)):
    if candies[i] + extracandies >= greatest:
        result.append(True)
    else:
        result.append(False)

print (result)