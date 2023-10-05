'''
Escreva um programa que converta a primeira letra de cada palavra de um arquivo 
em maiúscula e escreva o resultado na tela.
'''


def primeira_maiuscula(nome_arquivo: str) -> None:
    arquivo = open(nome_arquivo, 'r')

    for linhas in arquivo:
        cortar_palavras = linhas.split()
        for palavras in cortar_palavras:
            primeira_letra_maiuscula = palavras.capitalize()
            print(primeira_letra_maiuscula)

    arquivo.close()


arquivo_teste = 'exemplo.txt'
primeira_maiuscula(arquivo_teste)
