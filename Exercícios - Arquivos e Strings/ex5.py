# Tente outras formas de testar se uma palavra é um palíndromo. Tente outro fatiamento.

def e_palindromo(palavra: str) -> bool:
    palavra = palavra.lower()

    palavra_invertida = palavra[::-1]

    if palavra == palavra_invertida:
        return True
    else:
        return False


palavra1 = "reconhecer"
palavra2 = "python"
print(f"A palavra '{palavra1}' é um palíndromo? {e_palindromo(palavra1)}")
print(f"A palavra '{palavra2}' é um palíndromo? {e_palindromo(palavra2)}")
