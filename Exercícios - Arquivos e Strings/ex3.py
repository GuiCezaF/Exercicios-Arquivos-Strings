# Escreva um programa em Python que conte a quantidade de espaços em branco de uma string.

def contar_espacos_em_branco(texto: str) -> int:
    contador = 0
    
    for caractere in texto:
        if caractere.isspace():
            contador += 1
    
    return contador

texto = input("Digite uma string: ")

quantidade_espacos = contar_espacos_em_branco(texto)
print(f"A quantidade de espaços em branco na string é: {quantidade_espacos}")
