# Input: a = "11", b = "1"
# Output: "100"

a = "100101"
b = "1011"
carry = 0
arr = []

aa = list(a)
bb = list(b)

mayor = []

if len(aa) < len(bb):
    min_len = len(aa)
    restante = len(aa) - len(bb)
    mayor = aa
else:
    min_len = len(bb)
    restante = len(bb) - len(aa)
    mayor = bb

for i in range(min_len - 1, -1, -1):
    if bb[i] == "1" and aa[i] == "1":
        if carry >= 1:
            arr.append(1)
            mayor.pop(-1)
        else:
            arr.append(0)
            carry += 1
            mayor.pop(-1)

    elif bb[i] == "0" and aa[i] == "0":
        if carry >= 1:
            arr.append(1)
            carry -= 1
            mayor.pop(-1)
        else:
            arr.append(0)
            mayor.pop(-1)
    else:
        if carry >= 1:
            carry -= 1
            arr.append(0)
            mayor.pop(-1)
        else:
            arr.append(1)
            mayor.pop(-1)

mayor.reverse()


if restante >= 0:    
    for i in range(restante):
        if carry >= 1 and mayor[i] == "1":
            arr.append(0)
        elif carry >= 1 and mayor[i] == "0":
            arr.append(1)
            carry -= 1
        else:
            arr.append(mayor[i])

arr.int()

print (arr)