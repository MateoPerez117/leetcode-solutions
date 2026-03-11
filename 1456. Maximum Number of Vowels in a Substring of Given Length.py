# Input: s = "abciiidef", k = 3
# Output: 3

s = "abciiidef"
s = list(s)
k = 3
nums = []

for i in range(len(s)):
    if s[i] in "aeiou":
        nums.append(1)
    else:
        nums.append(0)

slwindow = sum(nums[:k])
maxoutput = slwindow

for i in range(k, len(nums)):
    slwindow = slwindow - nums[i - k] + nums[i]
    maxoutput = max(maxoutput, slwindow)

maxoutput = max(maxoutput, slwindow)

print (maxoutput)