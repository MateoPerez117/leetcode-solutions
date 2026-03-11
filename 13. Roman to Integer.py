s = "MCMXCIV"

valores = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

total = valores[s[-1]]

for i in range (len(s) - 2, -1, -1):
    if valores[s[i]] < valores[s[i + 1]]:
        total -= valores[s[i]]
    else:
        total += valores[s[i]]

print (total)