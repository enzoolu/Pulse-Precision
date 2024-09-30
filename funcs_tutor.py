from func_geral import forca_resposta

def criar_acesso(tutores):
    print(f"\n--- Cadastrar Novo Tutor (ID: {len(tutores) + 1}) ---")

    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    universidade = input("Digite o nome da universidade: ")
    senha = input("Digite a senha: ")

    tutores.append([nome, email, universidade, senha])

    print(f"\nTutor '{nome}' cadastrado com sucesso!\n")
    return tutores

def autenticar_tutor(tutores):
    if not tutores:
        print("Nenhum tutor cadastrado")
        return False

    print("\n--- Login ---")
    nome = input("Digite seu Nome: ")
    senha = input("Digite sua senha: ")

    for info in tutores:
        if info[0] == nome and info[3] == senha:
            print(f"\nLogin realizado com sucesso! Bem-vindo(a), {info[0]}.\n")
            return nome
    print("\nSenha incorreta. Tente novamente.\n")
    return False

def alunos_atribuidos(usuarios, tutor):
    alunos_encontrados = [aluno[0] for aluno in usuarios if aluno[4] == tutor]  # Nome dos alunos atribuídos a um tutor

    return alunos_encontrados

def avaliar_aluno(alunos):
    if alunos:
        print('Selecione um aluno(a): ')
        for i in range(len(alunos)):
            print(f'{i + 1} - {alunos[i]}')

        aluno = int(forca_resposta('Selecione uma opção: ', list(range(1, len(alunos) + 1)))) - 1

        criteios = [f'Precisão no Movimento: (0/10)\n', f'Precisão no Clique: (0/10)\n', f'Ritmo: (0/10)\n']

        notas = []

        for criteio in criteios:
            nota = int(forca_resposta(criteio, list(range(0, 11))))
            notas.append(nota)

        media = (notas[0] * 0.5) + (notas[1] * 0.3) + (notas[2] * 0.2)

        if media >= 8:
            nivel = 3
        elif media >= 6:
            nivel = 2
        else:
            nivel = 1

        print(f'Nivel Recomendado para o aluno {alunos[aluno]}: Nivel {nivel}')

    else:
        print('Nenhum aluno atribuido')

    return