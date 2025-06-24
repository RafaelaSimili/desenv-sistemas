nota = int(input("digite sua nota:"))
if (nota >= 80):
    print("Parabens")
elif (nota < 80 and nota >= 60):
    print("Pode melhorar")
elif (nota < 60):
    print("Recuperacao")


nota1 = int(input("digite sua nota:"))
nota2 = int(input("digite sua nota:"))
nota3 = int(input("digite sua nota:"))
nota4 = int(input("digite sua nota:"))

notafinal = (nota1 + nota2 + nota3 + nota4)/4
print("Sua media foi: ", notafinal)

if (notafinal >= 80):
    print("Excelente")
elif (notafinal < 80 and notafinal >= 60):
    print("Passou")
elif (notafinal < 60):
    print ("Ate ano que vem")


valor1 = int(input("digite seu valor:"))
valor2 = int(input("digite seu valor:"))

if (valor1 > valor2):
    print("O valor1 e maior que o valor2", valor1)
elif (valor2 > valor1):
    print("O valor2 e maior que o valor1", valor2)


