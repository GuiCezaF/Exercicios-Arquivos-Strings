'''
Escreva uma função que receba uma string como parâmetro e diga se se trata de um palíndromo
ou não. Na string devem ser ignorados os espaços em branco e as letras maiúsculas e minúsculas 
não são diferenciadas.
Por exemplo, a frase 'Seco de raiva coloco no colo caviar e doces' deve ser considerada
um palíndromo.
'''
def e_palindromo(palavra: str) -> bool:
    palavra = palavra.replace(" ", "").lower()

    palavra_invertida = palavra[::-1]

    if palavra == palavra_invertida:
        return True
    else:
        return False


palavra1 = "Seco de raiva coloco no colo caviar e doces"
print(f"A palavra '{palavra1}' é um palíndromo? {e_palindromo(palavra1)}")