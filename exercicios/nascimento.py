# Desenvolva um programa que recebe do usuário nome completo e ano 
# de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário 
# e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, 
# o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

from datetime import date
def nome_nasc():
    nome = input('Digite seu nome completo: ')
    while True:
        try:
            data_nasc = int(input('Digite o ano de nascimento: '))
            if 1922 <= data_nasc <= 2021:
                idade = date.today().year - data_nasc
                print(f'A idade de {nome} é {idade} anos')
                break
            else:
                print('Digite um ano de nascimento entre 1922 e 2021.')
        except ValueError:
            print('Ano de nascimento inválido! Por favor, insira um valor numérico válido.')

nome_nasc()