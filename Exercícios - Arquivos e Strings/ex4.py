'''
Escreva uma função que receba uma string como parâmetro e escreva-a invertida,
usando apenas o fatiamento. Ex.: 
'celacanto provoca maremoto ' imprime 'otomeram acovorp otnacalec'. 
Dica: o passo pode ser negativo.
'''


def invertida(string: str) -> str:
    string_invertida = string[::-1]
    return string_invertida


String_original = input('Digite uma string para ser invertida: ')

print(
    f'A string original: {String_original} invertida fica {invertida(String_original)}')
