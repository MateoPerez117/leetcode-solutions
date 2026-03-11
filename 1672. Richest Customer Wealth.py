# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6

accounts = [[6,59,64,19,30,76,71,86,90,25,56,17,19,72,61,56,24,40,35,39,67,28,52,11,82,72,8,82,81,47]]
suma = 0
maxi = sum(accounts[0])

for i in range (len (accounts)):
    maxi = max(maxi, suma)
    suma = sum(accounts[i])

print (maxi)