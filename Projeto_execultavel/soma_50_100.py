def somar_pares():
    soma = 0
    for numero in range(51, 99):
        if numero % 2 == 0:
            soma += numero
    return soma

soma_pares = somar_pares()
print("A soma de todos os números pares entre 50 e 100 é:", soma_pares)

print("\n")
print("\n")
input("Pressione Enter para sair...")