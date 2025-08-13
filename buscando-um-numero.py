#Elabore uma função que receba um número e uma lista. A função deve buscar o número na lista e retornar 'True' se o encontrar e 'False' caso contrário.
def buscar(numero, lista):
    for elemento in lista:
        if elemento == numero:
            return True
    return False

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
num = int(input('Digite um numero inteiro para buscar na lista: '))
resultado = buscar(num, numeros)
print(f"O número {num} está na lista? {resultado}")
