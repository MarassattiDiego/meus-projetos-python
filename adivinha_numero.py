import random

def jogar():
    numero_secreto = random.randint(1, 20)
    tentativas = 5

    print("Tente adivinhar o número entre 1 e 20. Você tem 5 tentativas.")

    for tentativa in range(1, tentativas + 1):
        chute = input(f"Tentativa {tentativa}: Digite seu palpite: ")

        if not chute.isdigit():
            print("Digite um número válido!")
            continue

        chute = int(chute)

        if chute < numero_secreto:
            print("Muito baixo!")
        elif chute > numero_secreto:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você acertou o número em {tentativa} tentativas.")
            break
    else:
        print(f"Suas tentativas acabaram. O número era {numero_secreto}.")

if __name__ == "__main__":
    jogar()
55