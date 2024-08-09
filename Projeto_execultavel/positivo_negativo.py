def separar_numeros(lista):
    positivos = []
    negativos = []

    for numero in lista:
        if numero >= 0:
            positivos.append(numero)
        else:
            negativos.append(numero)

    return positivos, negativos

lista = []
n = int(input("Quantos números você quer inserir? "))

for i in range(n):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista.append(numero)

positivos, negativos = separar_numeros(lista)

print("Números positivos:", positivos)
print("Números negativos:", negativos)

print("\n")
print("\n")
input("Pressione Enter para sair...")