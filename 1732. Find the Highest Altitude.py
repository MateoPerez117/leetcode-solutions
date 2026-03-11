# gain = [-5,1,5,0,-7]
# Output: 1

gain = [44,32,-9,52,23,-50,50,33,-84,47,-14,84,36,-62,37,81,-36,-85,-39,67,-63,64,-47,95,91,-40,65,67,92,-28,97,100,81]
best = gain[0]
suma = 0

for i in range (len(gain)):
    best = max(best, suma)
    suma += gain[i]
best = max(best, suma)

print (best)