import math

str1 = "ABCABC"
str2 = "ABC"

if str1 + str2 != str2 + str1:
    print ("")

else:
    str1lenght = len(str1)
    str2lenght = len(str2)

    g = math.gcd(str1lenght, str2lenght)

print (str1[:g])