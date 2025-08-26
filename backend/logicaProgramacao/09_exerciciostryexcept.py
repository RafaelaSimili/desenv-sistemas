# Usando (laços, função e try/except), crie um sistema para receber as 3 notas de um aluno e calcule a média anual se digitar algo sem ser número, tratar o erro.

def obter_nota(indice):
     while True:
        try:
            nota = float(input(f" Digite a {indice} nota do aluno: "))
            if 0 <= nota <= 10:
                return nota
            else:
                print(" A nota deve estar entre 0 e 10.")
        except ValueError:
            print(" Entrada inválida. Digite um número válido.")

def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    print(" Sistema de Cálculo de Média Anual \n")

    notas = []
    for i in range(1, 4):
        nota = obter_nota(i)
        notas.append(nota)

    media = calcular_media(notas)

    print(f"\n Média anual do aluno: {media:.2f}")

    if media >= 7:
        print(" Situação: Aprovado!")
    elif media >= 5:
        print(" Situação: Recuperação.")
    else:
        print(" Situação: Reprovado.")
        
# Usando (lista, função, laços, try/except), você deverá criar uma lista com números e mensagens se for número, adicionar a uma lista a parte. Se for mensagem, 
# tratar com o erro de tipo. Ao final, mostrar a lista só com os números.

def filtrar_numeros(lista_mista):
    numeros = []
    for item in lista_mista:
        try:
            numero = float(item) 
            numeros.append(numero)
        except ValueError:
            print(f" Erro: '{item}' não é um número e será ignorado.")
    return numeros

def main():
    print(" Filtro de Números em uma Lista\n")

    # Lista com misto de números e mensagens (strings)
    lista_mista = ['10', 'abc', '25.5', 'Olá', '50', '3.14', 'Python', '100']

    print(f" Lista original: {lista_mista}\n")

    # Processa e retorna apenas os números
    lista_numeros = filtrar_numeros(lista_mista)

    print(f"\n Lista apenas com números: {lista_numeros}") 

# Criar uma lista com cadastro de usuario

# Cadastrar
# Alterar                   Usar (função, lista, try/except, laços)
# Excluir 
# Listar 

def cadastrar():
    try:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        usuarios.append({"nome": nome, "idade": idade})
        print("Usuário cadastrado!\n")
    except ValueError:
        print("Erro: idade inválida.\n")

def listar():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return
    for i, u in enumerate(usuarios):
        print(f"{i}: {u['nome']}, {u['idade']} anos")
    print()

def alterar():
    listar()
    try:
        i = int(input("Qual número deseja alterar? "))
        nome = input("Novo nome: ")
        idade = int(input("Nova idade: "))
        usuarios[i] = {"nome": nome, "idade": idade}
        print("Usuário alterado!\n")
    except (ValueError, IndexError):
        print("Erro ao alterar usuário.\n")

def excluir():
    listar()
    try:
        i = int(input("Qual número deseja excluir? "))
        usuarios.pop(i)
        print("Usuário excluído!\n")
    except (ValueError, IndexError):
        print("Erro ao excluir usuário.\n")

while True:
    print("1-Cadastrar  2-Alterar  3-Excluir  4-Listar  5-Sair")
    op = input("Escolha: ")
    
    if op == "1":
        cadastrar()
    elif op == "2":
        alterar()
    elif op == "3":
        excluir()
    elif op == "4":
        listar()
    elif op == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida.\n")







