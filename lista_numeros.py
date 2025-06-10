def receber_numeros():
    numeros = []
    while True:
        entrada = input("Digite um número (ou 'sair' para terminar): ")
        if entrada.lower() == 'sair':
            break
        try:
            num = float(entrada)
            numeros.append(num)
        except ValueError:
            print("Digite um número válido!")

    return numeros

def mostrar_estatisticas(numeros):
    if len(numeros) == 0:
        print("Nenhum número foi digitado.")
        return

    numeros_ordenados = sorted(numeros)
    print("Números digitados (ordenados):", numeros_ordenados)
    print("Maior número:", max(numeros))
    print("Menor número:", min(numeros))

def main():
    print("Programa para receber números")
    lista = receber_numeros()
    mostrar_estatisticas(lista)

if __name__ == "__main__":
    main()
