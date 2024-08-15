class Cidade:
    def __init__(self, nome, populacao, sigla):
        self.nome = nome
        self.populacao = populacao
        self.sigla = sigla

    def __str__(self):
        return f"{self.nome} ({self.sigla}) - População: {self.populacao}"


class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    def adicionar_cidade(self, cidade):
        self.cidades.append(cidade)

    def calcular_populacao(self):
        return sum(cidade.populacao for cidade in self.cidades)

    def __str__(self):
        return f"{self.nome} ({self.sigla}) - População Total: {self.calcular_populacao()}"


cidade1 = Cidade("Maurilandia ", 14000, "GO")
cidade2 = Cidade("Morrinhos   ", 51000, "GO")
cidade3 = Cidade("Panama      ", 2600,  "GO")

cidade4 = Cidade("XiqueXique  ", 46000, "BH")
cidade5 = Cidade("Porto Seguro", 15000, "BH")
cidade6 = Cidade("Gequié      ", 156000,"BH")


estado1 = Estado("Goias", "GO")
estado1.adicionar_cidade(cidade1)
estado1.adicionar_cidade(cidade2)
estado1.adicionar_cidade(cidade3)

estado2 = Estado("Bahia", "BH")
estado2.adicionar_cidade(cidade5)
estado2.adicionar_cidade(cidade6)
estado2.adicionar_cidade(cidade4)

print(estado1)

cidades = [cidade1, cidade2, cidade3]
for cidade in cidades:
    print(cidade)
print("====================================")
print(estado2)

cidades2 = [cidade4, cidade5, cidade6]
for cidade2 in cidades2:
    print(cidade2)








