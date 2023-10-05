'''
Escreva um programa que salve uma tabela com a conversão de temperaturas
Celsius para Fahrenheit de 0 a 300.
'''

def celsius_para_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

def escrever_arquivo(nome_arquivo: str) -> None:
    arquivo = open(nome_arquivo, 'w')
    arquivo.write("Célsius para Fahrenheit\n")
    
    for celsius in range(0, 301, 10):
      fahrenheit = celsius_para_fahrenheit(celsius)
      arquivo.write(f'Em célsius = {celsius} || Fahrenheit = {fahrenheit}\n')
    arquivo.close()
    print('Tabela de conversão de temperaturas salva com sucesso!')

arquivo_teste = 'tabela_temperaturas.txt'
escrever_arquivo(arquivo_teste)