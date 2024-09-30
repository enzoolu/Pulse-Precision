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