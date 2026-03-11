arr = [1,2,2,1,1,3]
freq = {}

for i in range (len(arr)):
    if arr[i] in freq:
        freq[arr[i]] += 1
    else:
        freq[arr[i]] = 1

if len(freq.values()) == len(set(freq.values())):
    print(True)
else:
    print(False)