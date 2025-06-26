# Exibe mensagem de boas-vindas
print("Bem-vindo(a) ao Centro Comunitário")

# Lista vazia que armazenará os dicionários das doações
lista_doacao = []

# Variável global para gerar um id único para cada doação
id_global = 0

def cadastrar_doacao(id):
    nome = input("Digite o nome do doador: ")
    tipo = input("Digite o tipo da doação: ")
    data = input("Digite a data da doação: ")

    doacao = {
        "id": id,
        "nome": nome,
        "tipo": tipo,
        "data": data
    }

    lista_doacao.append(doacao)
    print("Doação cadastrada com sucesso!")

def consultar_doacao():
    while True:
        print("\n--- Menu de Consulta de Doações ---")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Tipo")
        print("4. Retornar ao menu")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if not lista_doacao:
                print("Nenhuma doação cadastrada.")
            else:
                for doacao in lista_doacao:
                    print(f"\nID: {doacao['id']}")
                    print(f"Nome: {doacao['nome']}")
                    print(f"Tipo: {doacao['tipo']}")
                    print(f"Data: {doacao['data']}")
        elif opcao == "2":
            id_busca = input("Digite o Id da Doação: ")
            encontrado = False
            for doacao in lista_doacao:
                if str(doacao["id"]) == id_busca:
                    print(doacao)
                    encontrado = True
                    break
            if not encontrado:
                print("Nenhuma doação encontrada com esse ID.")
        elif opcao == "3":
            tipo_busca = input("Digite o tipo da doação: ")
            encontrados = False
            for doacao in lista_doacao:
                if doacao["tipo"].lower() == tipo_busca.lower():
                    print(doacao)
                    encontrados = True
            if not encontrados:
                print("Nenhuma doação encontrada desse tipo.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def remover_doacao():
    while True:
        id_remover = input("Digite o Id da doação a ser removido: ")
        for doacao in lista_doacao:
            if str(doacao["id"]) == id_remover:
                lista_doacao.remove(doacao)
                print("Doação removida com sucesso!")
                return
        print("Id inválido. Tente novamente.")

# Menu principal
while True:
    print("\n=== Menu Principal ===")
    print("1. Cadastrar Doação")
    print("2. Consultar Doação")
    print("3. Remover Doação")
    print("4. Encerrar Programa")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        id_global += 1
        cadastrar_doacao(id_global)
    elif opcao == "2":
        consultar_doacao()
    elif opcao == "3":
        remover_doacao()
    elif opcao == "4":
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")

