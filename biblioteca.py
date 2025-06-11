biblioteca = [
    {"titulo": "Dom Casmurro", "alugado_por": "Diego"},
    {"titulo": "O Pequeno Príncipe", "alugado_por": None},
    {"titulo": "1984", "alugado_por": "João"},
    {"titulo": "Memórias Póstumas de Brás Cubas", "alugado_por": "Márcia"},
    {"titulo": "A Metamorfose", "alugado_por": None},
    {"titulo": "O Alienista", "alugado_por": "Maysa"},
]

def listar_livros():
    print("\n--- Lista de livros ---")
    for i, livro in enumerate(biblioteca, start=1):
        status = f"Alugado por {livro['alugado_por']}" if livro['alugado_por'] else "Disponível"
        print(f"{i}. {livro['titulo']} - {status}")

def adicionar_livro():
    titulo = input("Digite o título do livro para adicionar: ").strip()
    if titulo:
        biblioteca.append({"titulo": titulo, "alugado_por": None})
        print(f"Livro '{titulo}' adicionado com sucesso!")
    else:
        print("Título inválido.")

def alugar_livro():
    listar_livros()
    try:
        escolha = int(input("Escolha o número do livro para alugar: "))
        if 1 <= escolha <= len(biblioteca):
            livro = biblioteca[escolha - 1]
            if livro['alugado_por'] is None:
                nome = input("Digite seu nome para registrar o aluguel: ").strip()
                if nome:
                    livro['alugado_por'] = nome
                    print(f"Livro '{livro['titulo']}' alugado por {nome}.")
                else:
                    print("Nome inválido.")
            else:
                print(f"Livro já está alugado por {livro['alugado_por']}.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def devolver_livro():
    listar_livros()
    try:
        escolha = int(input("Escolha o número do livro para devolver: "))
        if 1 <= escolha <= len(biblioteca):
            livro = biblioteca[escolha - 1]
            if livro['alugado_por'] is not None:
                print(f"Livro '{livro['titulo']}' devolvido por {livro['alugado_por']}.")
                livro['alugado_por'] = None
            else:
                print("Este livro não está alugado.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    while True:
        print("\n--- Biblioteca ---")
        print("1 - Listar livros")
        print("2 - Adicionar livro")
        print("3 - Alugar livro")
        print("4 - Devolver livro")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_livros()
        elif opcao == '2':
            adicionar_livro()
        elif opcao == '3':
            alugar_livro()
        elif opcao == '4':
            devolver_livro()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
