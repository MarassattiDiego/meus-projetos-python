def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

print("Calculadora Simples")
print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = input("Digite o número da operação: ")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if op == "1":
    print("Resultado:", somar(n1, n2))
elif op == "2":
    print("Resultado:", subtrair(n1, n2))
elif op == "3":
    print("Resultado:", multiplicar(n1, n2))
elif op == "4":
    print("Resultado:", dividir(n1, n2))
else:
    print("Operação inválida.")
