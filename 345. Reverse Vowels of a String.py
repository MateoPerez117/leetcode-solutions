s = "Icecream"
sarrey = list(s)
s = s.lower()
vowels = []
holi = 0
diccionario = "aeiou"
for i in range (len(s)):
    if s[i] in diccionario:
        vowels.append(sarrey[i])

vowels.reverse()

for i in range(len(s)):
    if s[i] in diccionario:
        sarrey[i] = vowels[holi]
        holi += 1

sarrey = "".join(sarrey)

print (sarrey)