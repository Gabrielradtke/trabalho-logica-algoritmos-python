lista_livros = []
id_global = 0

# Função para exibir o menu principal
def menu_inicial():
    print('------------------------------------')
    print('Bem-vindo à Copiadora Gabriel Radtke')
    print('---------- Menu Principal ----------')
    print('      DIGITE A OPÇÃO DESEJADA!      ')
    print('1 - Cadastrar Livro                 ')
    print('2 - Consultar Livro                 ')
    print('3 - Remover Livro                   ')
    print('4 - Encerrar Programa               ')
    print('------------------------------------\n')

# Função para cadastrar livro
def cadastrar_livro(id_global):
    print('------------------------------------')
    print('---------- Menu Cadastro -----------')
    nome_livro = input('Insira o nome do livro: ')
    autor = input('Insira o nome do autor: ')
    editora = input('Insira o nome da editora: ')

    livro = {
        "id": id_global,
        "nome": nome_livro,
        "autor": autor,
        "editora": editora
    }

    lista_livros.append(livro)
    print('Livro cadastrado com sucesso!\n')

# Função para consultar livros
def consultar_livro():
    print('------------------------------------')
    print('---------- Menu Consultar ----------')
    while True:
        print('\nConsultar Livro: ')
        print('1. Consultar Todos')
        print('2. Consultar por Id')
        print('3. Consultar por Autor')
        print('4. Retornar ao menu')
        opcao = input("Digite o número da opção: \n")

        if opcao == '1':
            if not lista_livros:
                print("Nenhum livro cadastrado.")
            else:
                print('\n--- Todos os livros cadastrados ---')
                for livro in lista_livros:
                    print(f'Id: {livro["id"]}')
                    print(f'Livro: {livro["nome"]}')
                    print(f'Autor: {livro["autor"]}')
                    print(f'Editora: {livro["editora"]}')

        elif opcao == '2':
            try:
                id_busca = int(input('Digite o ID do livro: '))
                encontrado = False
                for livro in lista_livros:
                    if livro["id"] == id_busca:
                        print(f"ID: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: {livro['editora']}")
                        encontrado = True
                        break
                if not encontrado:
                    print('Livro não encontrado.')
            except ValueError:
                print('ID inválido. Digite um número.')

        elif opcao == '3':
            autor_busca = input("Digite o nome do autor: ").strip().lower()
            for livro in lista_livros:
                if livro['autor'].strip().lower() == autor_busca:
                    print(f"ID: {livro['id']}) Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: {livro['editora']}")
                else:
                    print('Autor não encontrado.')
        elif opcao == '4':
          break
          menu_inicial()

        else:
          print('Opção inválida!')

# Função para remover livro
def remover_livro():
    print('------------------------------------')
    print('----------- Menu Remover -----------')
    if not lista_livros:
        print("Nenhum livro para remover.")
        return
    try:
        id_remover = int(input('Digite o ID do livro a ser removido: '))
        for livro in lista_livros:
            if livro["id"] == id_remover:
                lista_livros.remove(livro)
                print('Livro removido com sucesso!\n')
                return
        print('ID não encontrado.')
    except ValueError:
        print('Digite um número válido.')

# Função para encerrar o programa
def encerrar_programa():
    print('Encerrando programa, até mais!')
    exit()

# Loop principal fora de uma função (main)
while True:
    menu_inicial()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif escolha == "2":
        consultar_livro()
    elif escolha == "3":
        remover_livro()
    elif escolha == "4":
        encerrar_programa()
        break
    else:
        print("Opção inválida. Tente novamente.")
