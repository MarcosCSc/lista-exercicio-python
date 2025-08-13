def somar_lista(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
resultado = somar_lista(numeros)
print(f"A soma dos números da lista é: {resultado}")