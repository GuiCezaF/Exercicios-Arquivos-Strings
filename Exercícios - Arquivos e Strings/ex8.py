'''
O Programa 6.10 só funciona bem com um nome composto de três partes.
Modifique o programa para que seja possível trabalhar com um número maior de partes.
'''


def formatar_nome(nome: str) -> str:
    partes_nome = nome.split()

    if len(partes_nome) >= 2:
        sobrenome = partes_nome[-1]
        primeiro_nome = partes_nome[0]
        inicial_segundo_nome = partes_nome[1][0] if len(
            partes_nome) > 2 else ''

        partes_adicionais = " ".join(partes_nome[2:])

        nome_formatado = f"{sobrenome}, {primeiro_nome} {inicial_segundo_nome}. {partes_adicionais}"
        return nome_formatado
    else:
        return "Nome inválido"


nome = 'João Carlos da Silva Pereira'
nome_formatado = formatar_nome(nome)
print(nome_formatado)
