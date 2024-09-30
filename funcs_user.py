from func_geral import *
def editar_usuario(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado para editar.\n")
        return

    print("\n--- Usuários Cadastrados ---\n")
    for idx, info in enumerate(usuarios):
        print(f'{idx + 1} - {info[0]}')

    usuario_id = int(forca_resposta("Selecione o número do usuário para editar: ", list(range(1, len(usuarios) + 1)))) - 1

    usuario_selecionado = usuarios[usuario_id]
    print(f"\n--- Informações do Usuário {usuario_id + 1}: ---")
    for idx, valor in enumerate(usuario_selecionado):
        print(f"{idx + 1} - {['Nome', 'Idade', 'Email', 'Semestre', 'Tutor'][idx]}: {valor}")

    opcao_edicao = int(forca_resposta("Selecione o número da informação que deseja alterar: ", list(range(1, len(usuario_selecionado) + 1))))

    novo_valor = input(f'Digite o novo valor para {["Nome", "Idade", "Email", "Semestre", "Tutor"][opcao_edicao - 1]}: ')

    if opcao_edicao == 2 or opcao_edicao == 4:
        novo_valor = int(novo_valor)

    usuario_selecionado[opcao_edicao - 1] = novo_valor
    print(f"\nInformação alterada com sucesso!\n")

    continuar = input('Deseja alterar mais alguma informação deste usuário? (s/n): ').lower()
    if continuar == 's':
        editar_usuario(usuarios)

def exibir_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return

    print("\n--- Usuários Cadastrados ---\n")
    for idx, info in enumerate(usuarios):
        print(f'Usuário {idx + 1}:')
        print(f"  Nome: {info[0]}")
        print(f"  Idade: {info[1]}")
        print(f"  Email: {info[2]}")
        print(f"  Semestre: {info[3]}")
        print(f"  Tutor: {info[4]}")
        print("-" * 30)

def cadastrar_usuario(usuarios):
    print(f'\n--- Cadastrar Usuário {len(usuarios) + 1} ---\n')

    nome = verifica_tipo('Digite o nome do usuário: ', 'str')
    idade = verifica_tipo('Digite a idade do usuário: ', 'int')
    email = verifica_tipo('Digite o email do usuário: ', 'str')
    semestre = verifica_tipo('Digite o semestre do usuário: ', 'int')
    tutor = verifica_tipo('Digite o tutor do usuário: ', 'str')

    usuarios.append([nome, idade, email, semestre, tutor])

    print(f'\nUsuário {nome} cadastrado com sucesso!\n')

    continuar = input('Deseja cadastrar outro usuário? (s/n): ').lower()

    if continuar == 's':
        cadastrar_usuario(usuarios)