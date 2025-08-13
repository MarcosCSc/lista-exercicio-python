def valores_unicos(lista):
    unicos = []
    for elemento in lista:
        if elemento not in unicos:
            unicos.append(elemento)
    return unicos

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
resultado = valores_unicos(numeros)
print(f"Lista com valores únicos: {resultado}")