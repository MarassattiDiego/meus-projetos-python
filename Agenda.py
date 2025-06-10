def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ").strip()
    telefone = input("Digite o telefone: ").strip()
    agenda.append({"nome": nome, "telefone": telefone})
    print(f"Contato {nome} adicionado!")

def listar_contatos(agenda):
    if not agenda:
        print("Agenda vazia!")
        return
    print("Contatos na agenda:")
    for i, contato in enumerate(agenda, start=1):
        print(f"{i}. {contato['nome']} - {contato['telefone']}")

def buscar_contato(agenda):
    busca = input("Digite o nome para buscar: ").strip().lower()
    encontrados = [c for c in agenda if busca in c['nome'].lower()]
    if encontrados:
        print("Contatos encontrados:")
        for c in encontrados:
            print(f"{c['nome']} - {c['telefone']}")
    else:
        print("Nenhum contato encontrado com esse nome.")

def menu():
    agenda = []
    while True:
        print("\n=== Mini Agenda ===")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato")
        print("4 - Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            adicionar_contato(agenda)
        elif escolha == "2":
            listar_contatos(agenda)
        elif escolha == "3":
            buscar_contato(agenda)
        elif escolha == "4":
            print("Saindo da agenda. Até mais!")
            break
        else:
            print("Opção inválida, tenta de novo.")

if __name__ == "__main__":
    menu()
