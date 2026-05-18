# Input: prices = [7,1,5,3,6,4]
# Output: 5

prices = [7,1,5,3,6,4]

minseen = float('inf')
maxprofit = float('-inf')

for i in range(len(prices)):
    minseen = min(minseen, prices[i])
    print (minseen)

    maxprofit = max(maxprofit, prices[i] - minseen)
    print (maxprofit)

print (maxprofit)