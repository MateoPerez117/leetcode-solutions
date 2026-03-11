word1 = "cabbba"
word2 = "abbccc"
freq = {}
freq2 = {}

for i in range (len(word1)):
    if word1[i] in freq:
        freq[word1[i]] += 1
    else:
        freq[word1[i]] = 1
    
for i in range (len(word2)):
    if word2[i] in freq2:
        freq2[word2[i]] += 1
    else:
        freq2[word2[i]] = 1

if set(freq.keys()) == set(freq2.keys()) and sorted(freq.values()) == sorted(freq2.values()):
    print(True)
else:
    print(False)