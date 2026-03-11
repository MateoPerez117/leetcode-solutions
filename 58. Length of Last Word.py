s = "a "
j = -1
xd = 0
flag = True
lenght = len(s)

while flag == True:
    if s[j] == " ":
        j -= 1
        lenght -= 1
        next
    elif s[j] != " ":
        while s[j] != " ":
            xd += 1
            j -= 1
            if xd == lenght:
                break
        flag = False

print (xd)
        


