- Crie um sistema de gerenciamento de petshop.
- Deverá ter os campos: nome, raça, idade, sexo, nome_dono, telefone_dono.
- O nome do arquivo json deve ser "Petshop.json".
- Faça o crud completo.

ARQUIVO = "Petshop.json"

def carregar():
    if os.path.exists(ARQ):
        with open(ARQ, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar(pets):
    with open(ARQ, "w", encoding="utf-8") as f:
        json.dump(pets, f, indent=4, ensure_ascii=False)

def listar(pets):
    if not pets:
        print("Nenhum pet cadastrado.")
    for i, p in enumerate(pets):
        print(f"{i+1} - {p['nome']} | {p['raca']} | {p['idade']} anos | {p['sexo']} | Dono: {p['nome_dono']} | Tel: {p['telefone_dono']}")

def adicionar():
    pet = {
        'nome': input("Nome do pet: "),
        'raca': input("Raça: "),
        'idade': input("Idade: "),
        'sexo': input("Sexo (M/F): "),
        'nome_dono': input("Nome do dono: "),
        'telefone_dono': input("Telefone do dono: "),
    }
    pets = carregar()
    pets.append(pet)
    salvar(pets)
    print("Pet adicionado!")

def atualizar():
    pets = carregar()
    listar(pets)
    try:
        idx = int(input("Número do pet para atualizar: ")) - 1
        pet = pets[idx]
    except (ValueError, IndexError):
        print("Número inválido.")
        return
    for chave in pet:
        novo = input(f"{chave} ({pet[chave]}): ")
        if novo:
            pet[chave] = novo if chave != 'sexo' else novo.upper()
    salvar(pets)
    print("Pet atualizado!")

def deletar():
    pets = carregar()
    listar(pets)
    try:
        idx = int(input("Número do pet para deletar: ")) - 1
        pets.pop(idx)
        salvar(pets)
        print("Pet deletado!")
    except (ValueError, IndexError):
        print("Número inválido.")

def menu():
    while True:
        print("\n1- Listar | 2- Adicionar | 3- Atualizar | 4- Deletar | 5- Sair")
        op = input("Opção: ")
        if op == '1':
            listar(carregar())
        elif op == '2':
            adicionar()
        elif op == '3':
            atualizar()
        elif op == '4':
            deletar()
        elif op == '5':
            break
        else:
            print("Opção inválida.")



