n = 10
uno = 1
output = 0

if n == 0:
    print(1)
else:
    binario = []

    while n > 0:
        residuo = n % 2
        binario.append(residuo)
        n = n // 2

    for i in range(len(binario)):
        if binario[i] == 0:
            output += uno
        uno *= 2
        
    print(output, binario)