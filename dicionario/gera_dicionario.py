def gerar_dicionario(frase):
    dicionario = {}
    for index, caractere in enumerate(frase, start=1):
        if caractere != " ":
            dicionario[str(index)] = caractere
    return dicionario

frase = input("Digite uma frase: ")

dicionario = gerar_dicionario(frase)

print("Dicionário gerado:")
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")