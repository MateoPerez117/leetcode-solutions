word1 = "ab"
word2 = "pqrs"

word3 = []

ultimo = 0

wordlenght1 = 0
wordlenght2 = 0

for i in range(len(word1)):
    wordlenght1 += 1
for i in range(len(word2)):
    wordlenght2 += 1

if wordlenght1 > wordlenght2:
    for i in range(wordlenght2):
        word3.append(word1[i])
        word3.append(word2[i])
            
    ultimo = wordlenght2
    agregar = word1[ultimo:] 
    word3.append(agregar)

    resultado = "".join(word3)

    print (resultado)

else:
    for i in range(wordlenght1):
        word3.append(word1[i])
        word3.append(word2[i])

    ultimo = wordlenght1
    agregar = word2[ultimo:] 
    word3.append(agregar)

    resultado = "".join(word3)

    print (resultado)