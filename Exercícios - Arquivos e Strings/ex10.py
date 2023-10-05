'''
Escreva um programa que converta todas as letras de um arquivo em maiúsculas
e escreva o resultado na tela.
'''


def converter_maiusculas_arquivo(nome_arquivo: str) -> None:
    arquivo = open(nome_arquivo, 'r')

    for linha in arquivo:
        linha_maiuscula = linha.upper()
        print(linha_maiuscula)

    arquivo.close()


arquivo_teste = 'exemplo.txt'
converter_maiusculas_arquivo(arquivo_teste)
