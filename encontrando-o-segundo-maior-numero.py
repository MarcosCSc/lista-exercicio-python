#Crie uma função que retorne o segundo maior número de uma lista. Considere que a lista pode ter números duplicados
def segundo_maior(lista):
    maior = int(-1)
    segundo = int(-1)
    for num in lista:
        if num > maior:
            segundo = maior
            maior = num
        elif num < maior and num > segundo:
            segundo = num
    return segundo

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
resultado = segundo_maior(numeros)
print(f"O segundo maior número da lista é: {resultado}")