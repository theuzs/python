estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50],
}
total = 0
print("Estoque atual:\n")
for produto, dados in estoque.items():
    print(f"Produto: {produto:7s}")
    print(f"  Quantidade: {dados[0]:5d}")
    print(f"  Preço unitário: R${dados[1]:6.2f}")
    print("------------------------")
print("-------------------------------------")

print("Início das vendas:\n")

while True:
    produto = input("Nome do produto (digite 'fim' para sair): ").strip().lower()
    if produto == "fim":
        break
    if produto in estoque:
        quantidade = int(input("Quantidade: "))
        if quantidade <= estoque[produto][0]:
            preço = estoque[produto][1]
            custo = preço * quantidade
            print(f"\n{produto:7s}: {quantidade:3d} x R${preço:6.2f} = R${custo:6.2f}")
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print("Quantidade solicitada não disponível.")
    else:
        print("Nome de produto inválido.")

print(f"\nCusto total das vendas: R${total:21.2f}\n")

print("Estoque atualizado:\n")
for produto, dados in estoque.items():
    print(f"Produto: {produto:7s}")
    print(f"  Quantidade: {dados[0]:5d}")
    print(f"  Preço unitário: R${dados[1]:6.2f}")
    print("------\n")

print("-------------------------------------")
