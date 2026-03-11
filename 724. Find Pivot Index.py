nums = [2,1,-1]
n = len(nums)
pref = [0] * (n + 1)
summ = -1

for i in range (n):
    pref[i + 1] = pref[i] + nums[i]

for i in range (len(pref) - 1):
    if pref[i] == pref[-1] - pref[i + 1]:
        summ = i
        break

print (summ)