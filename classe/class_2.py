class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome} - {self.telefone}"


class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = saldo
        self.clientes = clientes  # Lista de objetos Cliente
        self.numero = numero
        self.operacoes = []

    def resumo(self):
        clientes_info = ", ".join(str(cliente) for cliente in self.clientes)
        print(f"CC N°{self.numero} Saldo: {self.saldo:10.2f}")
        print(f"Clientes: {clientes_info}")
        print("*********************************")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente!")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC N° {self.numero}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n Saldo: {self.saldo:10.2f}\n")
        print("=================================")


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo e limite insuficientes!")


# Exemplo de uso
cliente1 = Cliente("João Silva", "1234-5678")
cliente2 = Cliente("Maria Oliveira", "8765-4321")
cliente3 = Cliente("Matheus Fagundes", "1234-4567")

conta1 = Conta([cliente1, cliente2, cliente3], 12345, 1000)
conta1.resumo()
conta1.deposito(500)
conta1.saque(200)
conta1.extrato()


conta2 = ContaEspecial([cliente1], 67890, 500, 200)
conta2.resumo()
conta1.deposito(500)
conta2.saque(600)
conta2.extrato()

conta3 = ContaEspecial([cliente3], 33330, 300, 200)
conta3.resumo()
conta1.deposito(500)
conta3.saque(600)
conta3.extrato()
