# Exibe mensagem de boas-vindas.
print("Bem-vindo(a) ao Centro Comunitário)


# Lista vazia que armazenará os dicionários das doações
lista_doacao = []


# Variável global para gerar um id único para cada doação
id_global = 0


def cadastrar_doacao(id):
   
    #Função para cadastrar uma nova doação.
    #Recebe um id (único para cada doação) e solicita ao usuário
    #que informe o nome, tipo e data do livro. Cria um dicionário
    #com esses dados e o adiciona na lista de doação.
   
    nome = input("Digite o nome do doador: ")
    tipo = input("Digite o tipo da doação: ")
    data = input("Digite a data da doação: ")
   
    # Cria o dicionário com os dados da doação
    doacao = {
        "id": id,
        "nome": nome,
        "tipo": tipo,
        "data": data
    }
   
    # Adiciona a doação na lista
    lista_doacao.append(doacao)
    print("Doação cadastrada com sucesso!")


def consultar_doacao():
 
    #Função para consultar as doações cadastradas.
    #Exibe um submenu que permite:
    #1. Consultar Todos as doações
    #2. Consultar por Id
    #3. Consultar por Data
    #4. Retornar ao menu principal
    #Se a opção digitada for inválida, a função repete a pergunta.
   
    while True:
        print("\n--- Menu de Consulta de Doações ---")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Data")
        print("4. Retornar ao menu")
        opcao = input("Escolha uma opção: ")


        if opcao == "1":
            # Consulta todas as doações
            if not lista_doacao:
                print("Nenhuma doação cadastrada.")
            else:
                for doacao in lista_doacao:
                    print(f"ID: {doacao['id']}")
                    print(f"nome: {doacao['nome']}")
                    print(f"Tipo: {doacao['tipo']}")
                    print(f"Data: {doacao['data']}\n")
        elif opcao == "2":
            # Consulta por Id
            id_busca = input("Digite o Id da Doação: ")
            encontrado = False
            for doação in lista_doacao:
                if str(doacao["id"]) == id_busca:
                    print(doacao)
                    encontrado = True
                    break
            if not encontrado:
                print("Nenhuma doação encontrada com esse ID.")
        elif opcao == "3":
            # Consulta por Tipo
            tipo_busca = input("Digite o tipo: ")
            encontrados = False
            for doacao in lista_doacao:
                # Comparação ignorando diferenças entre maiúsculas e minúsculas
                if doacao["tipo"].lower() == tipo_busca.lower():
                    print(doacao)
                    encontrados = True
            if not encontrados:
                print("Nenhuma doação encontrada desse tipo.")
        elif opcao == "4":
            # Retorna ao menu principal
            break
        else:
            print("Opção inválida. Tente novamente.")


def remover_doacao():
 
    #Função para remover uma doacao da lista.
    #Solicita o id da doacao a ser removido. Se o id for encontrado,
    #remove a doacao e exibe uma mensagem de sucesso. Caso contrário,
    #exibe "Id inválido" e repete a pergunta.
   
    while True:
        id_remover = input("Digite o Id da doação a ser removido: ")
        for doacao in lista_doacao:
            if str(doacao["id"]) == id_remover:
                lista_doacao.remove(doacao)
                print("Doação removida com sucesso!")
                return  # Sai da função após remoção
        print("Id inválido. Tente novamente.")


# Menu de opções
while True:
    print("\n=== Menu Principal ===")
    print("1. Cadastrar Doação")
    print("2. Consultar Doação")
    print("3. Remover Doação")
    print("4. Encerrar Programa")
    opcao = input("Escolha uma opção: ")


    if opcao == "1":
        # Incrementa o id global e chama a função de cadastro
        id_global += 1
        cadastrar_doacao(id_global)
    elif opcao == "2":
        # Chama a função de consulta de doações
        consultar_doacao()
    elif opcao == "3":
        # Chama a função para remover uma doação
        remover_doacao()
    elif opcao == "4":
        print("Encerrando o programa. Até logo!")
        break  # Sai do loop e encerra o programa
    else:
        print("Opção inválida. Tente novamente.")
