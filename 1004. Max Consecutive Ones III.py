nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

j = 0
k2 = k
slwindow = 0
maxoutput = 0

for i in range(len(nums)):
    slwindow += 1
    if nums[i] == 0:
        k2 -= 1

    while k2 < 0:
        slwindow -= 1
        if nums[j] == 0:
            k2 += 1
        j += 1

    maxoutput = max(maxoutput, slwindow)

print(maxoutput)

#como aqui tenemos el arreglo lleno de 1 
# podemos usar best = max(best, i - j + 1)