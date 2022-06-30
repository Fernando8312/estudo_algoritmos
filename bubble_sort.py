import random
l = random.sample(range(1199),20)
print(l)

def ordena(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
                #print(lista)
    return lista
print(ordena(l))

print("Primeiro branch")

