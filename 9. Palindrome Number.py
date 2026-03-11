x = 100001
newx = []
strx = str(x)
flag = True


for i in range(len(strx) -1, -1, -1):
    newx.append(strx[i])

for i in range(len(strx)):
    if newx[i] != strx[i]:
        flag = False
        print(flag)
        break

if flag == True:
    print(True)

