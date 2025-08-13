def menor_numero(lista):
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    return menor

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
print("Lista:", numeros)
print("Menor:", menor_numero(numeros))