def forca_resposta(texto, respostas):
    resposta = input(texto)
    if resposta.isnumeric():
        resposta = int(resposta)
        if resposta not in respostas:
            print('Opção inválida')
            return forca_resposta(texto, respostas)
        return resposta
    else:
        print('Digite uma opção numérica: ')
        return forca_resposta(texto, respostas)

def verifica_tipo(texto, tipo):
    resposta = input(texto)
    if tipo == 'int':
        if resposta.isnumeric():
            return resposta
        else:
            print('Digite uma opção numérica')
            return verifica_tipo(texto, tipo)
    else:
        if resposta.isnumeric():
            print('Digite uma opção não numérica')
            return verifica_tipo(texto, tipo)
        else:
            return resposta
