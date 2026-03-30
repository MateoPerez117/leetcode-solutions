# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0

def Find_needle_haystack(haystack: str, needle: str):
    k = 0
    contador = 0

    if needle not in haystack:
        return -1
    else:
        while True:
            if haystack[k] == needle[0]:
                holi = k
                j = k
                for i in range(len(needle)):
                    if haystack[j] != needle[i]:
                        k += 1
                        contador = 0
                        break
                    if haystack[j] == needle[i]:
                        contador +=1
                        j += 1
                        if contador == len(needle):
                            return holi
            else:
                    k += 1

a = Find_needle_haystack("sadbutsad", "sad")

print(a)