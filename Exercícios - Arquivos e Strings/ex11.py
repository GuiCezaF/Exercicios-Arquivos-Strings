'''
Escreva um programa que converta todas as letras de um arquivo em minúsculas
e escreva o resultado na tela.
'''


def converter_minusculas_arquivo(nome_arquivo: str) -> None:
    arquivo = open(nome_arquivo, 'r')

    for linhas in arquivo:
        linha_minuscula = linhas.lower()
        print(linha_minuscula)
    arquivo.close()


arquivo_teste = 'exemplo.txt'
converter_minusculas_arquivo(arquivo_teste)
