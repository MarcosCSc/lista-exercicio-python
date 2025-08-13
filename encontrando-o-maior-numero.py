#Escreva uma função que receba uma lista de números e retorne o maior número encontrado nela.
def maior_numero(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
resultado = maior_numero(numeros)
print(f"O maior número da lista é: {resultado}")