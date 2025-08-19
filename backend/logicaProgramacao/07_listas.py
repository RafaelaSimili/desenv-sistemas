# Crie uma lista de tarefas
# Adicione 5 tarefas na lista 
# Adicione uma tarefa na posição 2 da lista
# Remova a tarefa "lavar louça" da lista
# Remover a tarefa da posição 1 da lista

tarefas = []

tarefas.append("Lavar louça")
tarefas.append("Lavar banheiro")
tarefas.append("Passar pano")
tarefas.append("Limpar a casa")
tarefas.append("Limpar os móveis")

print(tarefas)

tarefas.insert(2, "lavar quintal")

print(tarefas)

tarefas.remove("Lavar louça")

print(tarefas)

tarefas.pop(1)

print(tarefas)

# Crie uma lista de alunos
# Mostre "olá" + nome de cada aluno

alunos = []

alunos.append("Rafaela")
alunos.append("João")
alunos.append("Helena")
alunos.append("Arthur")
alunos.append("Maria")
alunos.append("Miguel")
alunos.append("Alice")
alunos.append("Pedro")
alunos.append("Laura")
alunos.append("Theo")

for aluno in alunos:
    print("olá", aluno)

# Crie uma de 10 números
# Mostre a soma de todos os números da lista

numeros = []
soma = 0

numeros.append(1)
numeros.append(2)
numeros.append(3)
numeros.append(4)
numeros.append(5)
numeros.append(6)
numeros.append(7)
numeros.append(8)
numeros.append(9)
numeros.append(10)

for numero in numeros:
    soma += numero
print("soma:", soma)

# Crie uma lista de 20 números
# Diga quantos números pares e ímpares tem na lista

numeros = []

numeros.append(1)
numeros.append(2)
numeros.append(3)
numeros.append(4)
numeros.append(5)
numeros.append(6)
numeros.append(7)
numeros.append(8)
numeros.append(9)
numeros.append(10)
numeros.append(11)
numeros.append(12)
numeros.append(13)
numeros.append(14)
numeros.append(15)
numeros.append(16)
numeros.append(17)
numeros.append(18)
numeros.append(19)
numeros.append(20)

for numero in numeros:
    if numero % 2 == 0:
        print("Numero par", numero)
    else:
        print("Numero impar", numero)





