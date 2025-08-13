#Desenvolva uma função que receba uma lista de números inteiros e retorne uma nova lista contendo apenas os números pares
def numeros_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
resultado = numeros_pares(numeros)
print(f"Os números pares da lista são: {resultado}")