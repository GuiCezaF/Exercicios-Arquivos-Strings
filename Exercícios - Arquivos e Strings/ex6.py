'''
O teste de palíndromo desta seção tem um grande problema:
ele não diferencia maiúsculas de minúsculas.
Desse modo, 'Ovo' não seria identificado como palíndromo.
Como se pode consertar isso?
Pesquise a função de Python 'lower()' que transforma maiúsculas em minúsculas.
'''

def e_palindromo(palavra: str) -> bool:
    palavra = palavra.lower() # no exercicio anterior ja havia utilizado a função

    palavra_invertida = palavra[::-1]

    if palavra == palavra_invertida:
        return True
    else:
        return False