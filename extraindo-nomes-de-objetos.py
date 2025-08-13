class Pessoa:
    def __init__(self, nome):
        self.nome = nome

def extrair_nomes(lista_objetos):
    nomes = []
    for objeto in lista_objetos:
        nomes.append(objeto.nome)
    return nomes

pessoas = [
    Pessoa("Marcos"),
    Pessoa("Mario"),
    Pessoa("David"),
    Pessoa("José"),
    Pessoa("Claudinete")
]
resultado = extrair_nomes(pessoas)
print(f"Lista de nomes: {resultado}")