class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Meu nome é {self.nome} e eu tenho {self.idade} anos."

# Criando objetos da classe Pessoa
pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

# Acessando os atributos e métodos dos objetos
print(pessoa1.nome)          # Output: João
print(pessoa2.idade)         # Output: 25
print(pessoa1.saudacao())   # Output: Meu nome é João e eu tenho 30 anos.
print(pessoa2.saudacao())   # Output: Meu nome é Maria e eu tenho 25 anos.
