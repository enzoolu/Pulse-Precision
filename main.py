from funcs_tutor import *
from funcs_user import *
from func_geral import forca_resposta

usuarios = []

tutores = []

while True:
    opcoes_menu = (f'*----PULSE PRECISION----*\n\n'
                f'1 - Acessar menu de cadastro\n'
                f'2 - Acessar menu de Tutor\n'
                f'3 - Sair do Programa\n')

    resp = forca_resposta(opcoes_menu, list(range(1,4)))

    if resp == 1:
        while True:
            opcoes = (f'Opções: \n'
                    f'1 - Ver usuários cadastrados\n'
                    f'2 - Cadastrar novo usuário\n'
                    f'3 - Editar informações de usuário\n'
                    f'4 - Sair do menu de cadastro\n')

            resp = forca_resposta(opcoes, list(range(1,5)))

            if resp == 1:
                exibir_usuarios(usuarios)
            elif resp == 2:
                cadastrar_usuario(usuarios)
            elif resp == 3:
                editar_usuario(usuarios)
            else:
                break

    elif resp == 2:
        while True:
            login = (f'1 - Fazer Login\n'
                     f'2 - Criar acesso\n')

            resp = forca_resposta(login, list(range(1, 3)))

            if resp == 1:
                nome = autenticar_tutor(tutores)

                if nome != False:
                    while True:
                        opcoes = (f'Opções: \n'
                                  f'1 - Ver alunos atribuidos\n'
                                  f'2 - Avaliar aluno\n'
                                  f'4 - Sair do menu de tutor\n')

                        resp = forca_resposta(opcoes, list(range(1, 5)))

                        if resp == 1:
                            alunos = alunos_atribuidos(usuarios, nome)

                            if alunos:
                                print(f"\nAlunos atribuídos ao tutor {nome}:")
                                for i in range(len(alunos)):
                                    print(f"{i + 1} - {alunos[i]}")
                            else:
                                print(f"\nNenhum aluno encontrado.")

                        elif resp == 2:
                            alunos = alunos_atribuidos(usuarios, nome)
                            avaliar_aluno(alunos)
                        else:
                            break

                else:
                    break
            else:
                criar_acesso(tutores)

    else:
        break