agenda = []
# Variável para marcar uma alteração na agenda
alterada = False

def pede_nome(padrao=""):
    # Solicita o nome ao usuário; se não fornecido, usa o valor padrão
    nome = input("Nome: ")
    if nome == "":
        nome = padrao
    return nome

def pede_telefone(padrao=""):
    # Solicita o telefone ao usuário; se não fornecido, usa o valor padrão
    telefone = input("Telefone: ")
    if telefone == "":
        telefone = padrao
    return telefone

def pede_email(padrao=""):
    # Solicita o email ao usuário; se não fornecido, usa o valor padrão
    email = input("Email: ")
    if email == "":
        email = padrao
    return email

def pede_aniversario(padrao=""):
    # Solicita a data de aniversário ao usuário; se não fornecida, usa o valor padrão
    aniversario = input("Data de aniversário: ")
    if aniversario == "":
        aniversario = padrao
    return aniversario

def pede_endereco(padrao=""):
    # Solicita o endereço ao usuário; se não fornecido, usa o valor padrão
    endereco = input("Endereço: ")
    if endereco == "":
        endereco = padrao
    return endereco

def pede_cidade(padrao=""):
    # Solicita a cidade ao usuário; se não fornecida, usa o valor padrão
    cidade = input("Cidade: ")
    if cidade == "":
        cidade = padrao
    return cidade

def pede_uf(padrao=""):
    # Solicita a UF ao usuário; se não fornecida, usa o valor padrão
    uf = input("UF: ")
    if uf == "":
        uf = padrao
    return uf

def mostra_dados(nome, telefone, email, aniversario, endereco, cidade, uf):
    # Exibe os dados de contato formatados
    print(
        f"Nome: {nome}\nTelefone: {telefone}\n"
        f"Email: {email}\nAniversário: {aniversario}\n"
        f"Endereço: {endereco}\nCidade: {cidade}\nUF: {uf}\n"
    )

def pede_nome_arquivo():
    # Solicita o nome do arquivo ao usuário
    return input("Nome do arquivo: ")

def pesquisa(nome):
    # Procura o nome na agenda e retorna o índice se encontrado, caso contrário, retorna None
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

def novo():
    # Adiciona um novo contato à agenda se o nome não existir
    global agenda, alterada
    nome = pede_nome()
    if pesquisa(nome) is not None:
        print("Nome já existe!")
        return
    telefone = pede_telefone()
    email = pede_email()
    aniversario = pede_aniversario()
    endereco = pede_endereco()
    cidade = pede_cidade()
    uf = pede_uf()
    agenda.append([nome, telefone, email, aniversario, endereco, cidade, uf])
    alterada = True

def confirma(operacao):
    # Solicita confirmação ao usuário para a operação especificada (S/N)
    while True:
        opcao = input(f"Confirma {operacao} (S/N)? ").upper()
        if opcao in "SN":
            return opcao
        else:
            print("Resposta inválida. Escolha S ou N.")

def apaga():
    # Remove um contato da agenda após confirmação do usuário
    global agenda, alterada
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        if confirma("apagamento") == "S":
            del agenda[p]
            alterada = True
    else:
        print("Nome não encontrado.")

def altera():
    # Altera os dados de um contato existente após confirmação do usuário
    global alterada
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        email = agenda[p][2]
        aniversario = agenda[p][3]
        endereco = agenda[p][4]
        cidade = agenda[p][5]
        uf = agenda[p][6]
        print("Encontrado:")
        mostra_dados(nome, telefone, email, aniversario, endereco, cidade, uf)
        nome = pede_nome(nome)  # Se nada for digitado, mantém o valor
        telefone = pede_telefone(telefone)
        email = pede_email(email)
        aniversario = pede_aniversario(aniversario)
        endereco = pede_endereco(endereco)
        cidade = pede_cidade(cidade)
        uf = pede_uf(uf)
        if confirma("alteração") == "S":
            agenda[p] = [nome, telefone, email, aniversario, endereco, cidade, uf]
            alterada = True
    else:
        print("Nome não encontrado.")

def lista():
    # Lista todos os contatos na agenda com suas posições
    print("\nAgenda\n\n------")
    for posicao, e in enumerate(agenda):
        print(f"\nPosição: {posicao}")
        mostra_dados(e[0], e[1], e[2], e[3], e[4], e[5], e[6])
    print("------\n")

def le_ultima_agenda_gravada():
    # Lê a última agenda gravada, se disponível
    ultima = ultima_agenda()
    if ultima is not None:
        leia_arquivo(ultima)

def ultima_agenda():
    # Retorna o nome do último arquivo de agenda gravado ou None se não existir
    try:
        with open("ultima agenda.dat", "r", encoding="utf-8") as arquivo:
            ultima = arquivo.readline().strip()
    except FileNotFoundError:
        return None
    return ultima

def atualiza_ultima(nome):
    # Atualiza o arquivo que armazena o nome do último arquivo de agenda gravado
    with open("ultima agenda.dat", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}\n")

def leia_arquivo(nome_arquivo):
    # Lê e carrega os dados da agenda a partir de um arquivo
    global agenda, alterada
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        agenda = []
        for l in arquivo.readlines():
            dados = l.strip().split("#")
            if len(dados) == 7:
                nome, telefone, email, aniversario, endereco, cidade, uf = dados
                agenda.append([nome, telefone, email, aniversario, endereco, cidade, uf])
    alterada = False

def le():
    # Lê e carrega uma agenda de um arquivo, perguntando se deve salvar alterações não salvas
    global alterada
    if alterada:
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")
        if confirma("gravação") == "S":
            grava()
    print("Ler\n---")
    nome_arquivo = pede_nome_arquivo()
    leia_arquivo(nome_arquivo)
    atualiza_ultima(nome_arquivo)

def ordena():
    # Ordena a agenda por nome usando o método de bolhas
    global alterada
    fim = len(agenda)
    while fim > 1:
        i = 0
        trocou = False
        while i < (fim - 1):
            if agenda[i][0].lower() > agenda[i + 1][0].lower():
                # Troca os elementos se estiver fora de ordem
                temp = agenda[i + 1]
                agenda[i + 1] = agenda[i]
                agenda[i] = temp
                trocou = True
            i += 1
        if not trocou:
            break
    alterada = True

def grava():
    # Grava a agenda atual em um arquivo e atualiza o nome do último arquivo gravado
    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return
    print("Gravar\n------")
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}#{e[2]}#{e[3]}#{e[4]}#{e[5]}#{e[6]}\n")
    atualiza_ultima(nome_arquivo)
    alterada = False

def valida_faixa_inteiro(pergunta, inicio, fim):
    # Solicita um número inteiro dentro de um intervalo especificado
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

def menu():
    # Exibe o menu de opções e valida a escolha do usuário
    print("""
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Le
7 - Ordena por nome
0 - Sai
""")
    print(f"\nNomes na agenda: {len(agenda)} Alterada: {alterada}\n")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)

# Início do programa
le_ultima_agenda_gravada()
while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        le()
    elif opcao == 7:
        ordena()
