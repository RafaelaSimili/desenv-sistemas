salario = float(input("digite seu salario: "))
salarioanual = salario * 12
print ("salario anual: " , salarioanual)

if salario >= 5000:
    imposto = salario * 0.08
elif salario < 5000:
    imposto = salario * 0.05
print("imposto: " , imposto)