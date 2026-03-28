# Input: n = 4
# Output: 10
# Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.


n = 10


day = 1
days = 0
output = 0


for i in range (n):
    output = output + day
    day +=1
    days += 1


    if days == 7:
        days = 0
        day -= 6




print (output)


