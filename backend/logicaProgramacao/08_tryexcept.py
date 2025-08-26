# "Try-except" é uma estrutura em programação usada para lidar com erros (chamados exceções) que podem ocorrer durante a execução de um código, evitando que o programa 
# pare abruptamente. O bloco try contém o código que pode gerar um erro, e o bloco except é executado se uma exceção específica ocorrer nesse código, permitindo que o
# programa seja tratado de forma mais robusta. 

# Como funciona:

# 1. Bloco try:
# É aqui que você coloca o código que você suspeita que possa causar um erro. Por exemplo, uma divisão por zero ou a tentativa de abrir um arquivo inexistente. 

# 2. Ocorrência de Erro:
# Se um erro (exceção) acontecer dentro do bloco try, o programa para a execução desse bloco imediatamente. 

# 3. Bloco except:
# O programa então vai procurar um bloco except que corresponda ao tipo de erro ocorrido. 

# 4. Execução do except:
# Se um except correspondente for encontrado, o código dentro dele é executado. Por exemplo, você pode imprimir uma mensagem informativa, como "Erro: Divisão por zero
# não permitida", ou realizar alguma ação de recuperação. 

# 5. Sem Erro:
# Se o código dentro do bloco try for executado com sucesso, sem gerar nenhuma exceção, o bloco except é ignorado. 

# Tipos de Except

# Os tipos de "except" referem-se às diferentes categorias de erros (exceções) que uma aplicação pode encontrar e que podem ser tratadas usando a instrução try...except
# em linguagens de programação como Python. Existem exceções específicas, como ValueError para valores inadequados ou ZeroDivisionError para divisão por zero, e classes
# mais genéricas, como Exception e BaseException, que podem ser usadas para capturar exceções mais amplas ou agrupar múltiplos erros. 

# Exceções Específicas (Exemplos em Python):

# Estes são tipos de exceções que identificam causas de erro mais precisas: 

# ValueError: Ocorre quando um objeto tem o tipo correto, mas um valor inapropriado. 

# ZeroDivisionError: Lançada quando se tenta dividir um número por zero. 

# IndexError: Ocorre ao tentar aceder a um índice que não existe numa sequência (lista, por exemplo).

# KeyError: Surge quando uma chave não é encontrada num dicionário. 

# KeyboardInterrupt: Lançada quando o utilizador pressiona CTRL + C ou um botão de interrupção. 

# Exceções Genéricas

# Estas classes são mais amplas e servem como bases para exceções específicas: 

# Exception: Uma classe base para exceções que a maioria dos programas precisa lidar. 

# BaseExceptionGroup: Usada para agrupar múltiplos erros não relacionados, permitindo que sejam tratados como um grupo. 

# Exemplo em Python: 

try:
  # Código que pode causar um erro
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite outro número: "))
  resultado = num1 / num2
  print(f"O resultado da divisão é: {resultado}")
except ValueError:
  # Executado se o usuário não digitar um número
  print("Erro: Por favor, digite apenas números válidos.")
except ZeroDivisionError:
  # Executado se o usuário tentar dividir por zero
  print("Erro: Não é possível dividir por zero.")
except Exception as e:
  # Captura qualquer outro erro não especificado
  print(f"Ocorreu um erro inesperado: {e}")