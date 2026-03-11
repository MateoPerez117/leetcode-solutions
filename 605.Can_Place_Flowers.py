# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

flowerbed = [0,0,1,0,1]
n = 1

flowerbed.insert(0, 0)
flowerbed.append(0)

for i in range(len(flowerbed) - 2):
    if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0 :
        flowerbed[i+1] += 1
        n = n - 1

    print (flowerbed[i])

    if n == 0:
        break

if n == 0:
    print(True)
else:
    print(False)
