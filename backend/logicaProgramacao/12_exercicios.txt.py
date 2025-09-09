1. # Eu, como dono de uma padaria, quero um sistema onde eu possa cadastrar meus produtos, além de poder listar, alterar em caso de error e excluir quando
# acabar o estoque. Quero também que tenha um menu onde eu possa ver as opções possíveis.

 produtos = []

def menu():                                             #FAZ ESSE "DEF" PRA APARECER O MENU QUANDO EXECUTAR
    print("MENU")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Alterar produto")
    print("4. Excluir produto")
    print("5. Sair")

def cadastrar():                                        #FAZ ESSE "DEF" PRA APARECER O MENU CADASTRAR QUANDO EXECUTAR DEPOIS ELE VAI TE PEDIR O NOME COM O INPUT
    nome = input("Nome do produto: ")
    produtos.append(nome)                               #é um método da lista em Python que adiciona um item no final da lista.
    print("Produto cadastrado!")

def listar():                                           #FAZ ESSE "DEF" PRA APARECER O MENU CADASTRAR QUANDO EXECUTAR DEPOIS ELE VAI TE PEDIR O NOME COM O INPUT
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for i, nome in enumerate(produtos):             #Esse é um laço for com enumerate(), usado para percorrer a lista de produtos.
            print(f"{i} - {nome}")                      #Mostra o índice (ID) e o nome do produto

def alterar():
    listar()                                             #Chama a função listar() antes de tudo, para mostrar ao usuário quais produtos existem e seus respectivos IDs (índices)
    try:
        i = int(input("ID do produto para alterar: "))  #Pede ao usuário para digitar o ID (índice) do produto que ele quer alterar.
        if 0 <= i < len(produtos):                      #Verifica se o ID digitado está dentro do intervalo válido da lista:
            novo_nome = input("Novo nome: ")            #Se o ID for válido, o programa pede ao usuário para digitar o novo nome do produto.
            produtos[i] = novo_nome                     #produtos[i] acessa o produto na posição i da lista.
            print("Produto alterado!")
        else:
            print("ID inválido.")
    except ValueError:                                      #ocorre quando uma função recebe um argumento com o tipo de dado correto, mas com um valor inadequado para a operação
        print("Por favor, digite um número válido.")

def excluir():
    listar()
    try:
        i = int(input("ID do produto para excluir: "))   #Pede ao usuário que digite o ID (índice) do produto que ele deseja excluir.
        if 0 <= i < len(produtos):                       #Verifica se o número digitado (i) está dentro de uma faixa válida de índices da lista produtos.
            produtos.pop(i)                              #Remove o produto da lista produtos na posição i.
            print("Produto excluído!")
        else:                                              #Se o número digitado não for um índice válido (menor que 0 ou maior/igual ao tamanho da lista), essa mensagem será exibida.
            print("ID inválido.")
    except ValueError:                                      #ocorre quando uma função recebe um argumento com o tipo de dado correto, mas com um valor inadequado para a operação
        print("Por favor, digite um número válido.")

while True:                                         #Isso cria um laço infinito, ou seja, o programa vai continuar rodando até que o usuário escolha sair
    menu()
    opcao = input("Opção: ")
    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        alterar()
    elif opcao == '4':
        excluir()
    elif opcao == '5':
        print("Saindo...")
        break
    else:
        print("O


 2. # Sou o dono de uma concessionária e vi o sistema do dono da padaria. Gostaria de um sistema igual para meus carros.

carros = []

carros = []

def mostrar_menu():
    print("MENU CONCESSIONÁRIA")
    print("1. Cadastrar carro")
    print("2. Listar carros")
    print("3. Alterar carro")
    print("4. Excluir carro")
    print("5. Sair")

def cadastrar():
    nome = input("Nome do carro: ")
    carros.append(nome)
    print("Carro cadastrado com sucesso!")

def listar():
    if not carros:
        print("Nenhum carro cadastrado.")
        return
    print("\n--- Lista de carros ---")
    for i, nome in enumerate(carros):
        print("{i} - {nome}")

def alterar():
    listar()
    try:
        i = int(input("Digite o índice do carro que deseja alterar: "))
        if 0 <= i < len(carros):
            novo_nome = input("Digite o novo nome do carro: ")
            carros[i] = novo_nome
            print("Carro alterado com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def excluir():
    listar()
    try:
        i = int(input("Digite o índice do carro que deseja excluir: "))
        if 0 <= i < len(carros):
            carros.pop(i)
            print("Carro excluído com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

while True:
    mostrar_menu()
    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            alterar()
        elif opcao == 4:
            excluir()
        elif opcao == 5:
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Digite um número de 1 a 5.")
    except ValueError:
        print("Entrada inválida. Digite ap


3. # Explique porque quando tem mais de um atributo(variável), torna-se dificil/complicado o uso de arquivos txt para guardar informações.

# O uso de arquivos .txt para guardar múltiplos atributos de forma eficiente é complicado porque eles exigem a definição e o uso de um formato
# de organização (como separadores de vírgula ou ponto e vírgula) para que os dados possam ser separados e interpretados corretamente. Isso pode
# levar a erros de análise, dificuldade na leitura humana e na manipulação programática dos dados, além de dificultar a adição ou modificação de 
# novas informações sem reestruturar o arquivo. 

# Problemas comuns ao usar arquivos .txt com múltiplos atributos:

# Dificuldade de Análise:
# Para um programa, ler e interpretar cada linha de um arquivo .txt que contém diversos atributos exige o conhecimento exato do formato (qual separador 
# foi usado, a ordem dos atributos, etc.) para separar as informações corretamente. 

# Ambiguidades e Erros:
# Se o formato não for padronizado, como usar diferentes separadores em linhas diferentes ou incluir o separador dentro de um dos campos de texto, a 
# interpretação dos dados pode gerar erros. 

# Manutenção do Formato:
# Cada vez que você precisa adicionar, remover ou modificar um atributo, todo o arquivo .txt pode precisar ser reestruturado para manter a consistência,
# o que pode ser trabalhoso. 

# Complexidade na Leitura Humana:
# Embora o formato seja legível, a visualização e a compreensão de grandes volumes de dados com múltiplos atributos se tornam rapidamente desorganizadas. 

# Dependência da Programação:
# Para trabalhar com esses dados, a programação se torna complexa, exigindo algoritmos específicos para cada tipo de arquivo .txt, o que não é escalável
# para diferentes tipos de estruturas de dados. 


