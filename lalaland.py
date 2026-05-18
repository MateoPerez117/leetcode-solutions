
def ejercicio1(word1,word2 ):

    list1 = list(word1)
    list2 = list(word2)
    restuldo = []

    for i in range(len(list1)):
        restuldo.append(list1[i])
        restuldo.append(list2[i])


    resultado2 = "".join(restuldo)

    return (resultado2)

print(ejercicio1('abc', 'pqr'))