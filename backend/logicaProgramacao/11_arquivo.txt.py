# Um arquivo TXT é um ficheiro de texto simples, que não contém formatação, como tipos de letra, tamanhos, cores ou imagens, e é compatível com qualquer sistema 
# operativo e software de texto básico. É usado para armazenar informações textuais e é útil para dados de configuração, código-fonte e outras informações que
# precisam ser lidas facilmente por computadores e humanos, sem a interferência de formatação complexa. 

# Para alterar um registo num ficheiro .txt, abra o ficheiro com um editor de texto como o Bloco de Notas, faça as alterações desejadas e guarde o ficheiro.  
# Para excluir um registo, pode reescrever todo o ficheiro numa nova cópia, omitindo o registo a excluir, e depois substituir o ficheiro antigo pelo novo, ou 
# pode copiar todos os registos para um novo ficheiro, exceto o que pretende eliminar, e então renomear o novo ficheiro para o nome do original. 

# Para alterar um registo:

# 1. Abra o ficheiro TXT: Clique com o botão direito do mouse no ficheiro .txt e selecione "Abrir" ou "Editar" no menu contextual. Selecione um editor de texto, 
# como o Bloco de Notas (Windows) ou o TextEdit (macOS).

# 2. Faça as suas alterações: Localize o texto ou registo que pretende alterar e modifique-o diretamente no editor de texto. 

# 3. Guarde o ficheiro: Vá em "Ficheiro" e clique em "Guardar" para aplicar as alterações. 

# Para excluir um registo:

# Excluir registos num ficheiro .txt geralmente envolve a criação de um novo ficheiro ou a reescrita do existente. 

# Método 1: Reescrita para um novo ficheiro (Recomendado)

# 1. Abra o ficheiro: com um editor de texto. 

# 2. Copie todo o conteúdo: do ficheiro para um novo ficheiro, excluindo a linha ou o registo que quer remover. 

# 3. Guarde este novo ficheiro: com um nome temporário, por exemplo, novo_ficheiro.txt. 

# 4. Guarde este novo ficheiro: com um nome temporário, por exemplo, novo_ficheiro.txt. 

# 5. Renomeie o novo_ficheiro.txt: para o nome do ficheiro original. 

# Método 2: Para um ficheiro de texto simples

# Método manual: Se for apenas um registo e o ficheiro for pequeno, pode simplesmente apagá-lo manualmente no editor de texto e guardar o ficheiro.

# Nota: Em muitas linguagens de programação, para remover uma linha de um ficheiro, o processo é semelhante: ler o ficheiro, escrever as linhas necessárias num novo ficheiro, 
# apagar o original e renomear o novo ficheiro. 

# Exemplo: 

carros = []
id_atual = 1

def cadastrar():
    global id_atual
    carros.append({"id": id_atual, "modelo": input("Modelo: ")})
    id_atual += 1

def listar():
    for c in carros: print(c)

def alterar():
    id_busca = int(input("ID: "))
    for c in carros:
        if c["id"] == id_busca:
            c["modelo"] = input("Novo modelo: ") or c["modelo"]

def excluir():
    id_busca = int(input("ID: "))
    global carros
    carros = [c for c in carros if c["id"] != id_busca]

while True:
    op = input("1-Cadastrar 2-Listar 3-Alterar 4-Excluir 5-Sair: ")
    if op == "1": cadastrar()
    elif op == "2": listar()
    elif op == "3": alterar()
    elif op == "4": excluir()
    elif op == "5": break
