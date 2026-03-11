digits = [9]

numero = 0
for i in digits:
    numero = numero * 10 + i
numero += 1

h = list(str(numero))

digits = [int(d) for d in str(numero)]

print(digits)