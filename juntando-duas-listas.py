def concatenar_listas(natureza, tecnologia):
    lista3 = []
    for elemento in natureza:
        lista3.append(elemento)
    for elemento in tecnologia:
        lista3.append(elemento)
    return lista3

natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]
resultado = concatenar_listas(natureza, tecnologia)
print(f"Lista concatenada: {resultado}")