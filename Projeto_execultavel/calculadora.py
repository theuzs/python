n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
print("Escolha a operação: ")
print("[1]-somar")
print("[2]-subtrair")
print("[3]-multiplicar")
print("[4]-sair")
opcao = int(input('Qual opção desejada?'))
while opcao < 1 or opcao > 4:
    opcao = int(input('Opção Inválida. Redigite:'))

while opcao != 4:
    if opcao == 1:
        r = n1 + n2
    elif opcao == 2:
        r = n1 - n2
    elif opcao == 3:
        r = n1 * n2

    print('Resultado = {}'.format(r))

    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    print("Escolha a operação: ")
    print("[1]-somar")
    print("[2]-subtrair")
    print("[3]-multiplicar")
    print("[4]-sair")
    opcao = int(input('Qual opção desejada?'))
    while opcao < 1 or opcao > 4:
        opcao = int(input('Opção Inválida. Redigite:'))

print("\n")
print("\n")
input("Pressione Enter para sair...")