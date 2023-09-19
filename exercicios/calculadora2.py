
def calculadora(valor_1, valor_2, operacao):
    if operacao == 0:
        exit
    elif operacao == 1:
        return valor_1 + valor_2
    elif operacao == 2:
        return valor_1 - valor_2
    elif operacao == 3:
        return valor_1 * valor_2
    elif operacao == 4:
        return valor_1 / valor_2
    

valor_1 = int(input('Digite o 1º valor: '))
valor_2 = int(input('Digite o 2º valor: '))


def menu():
    print('''
    1: Soma
    2: Subtração
    3: Multiplicação
    4: Divisão
    0: Sair
    ''')

    operacao = int(input('Digite a operação desejada: '))

    operacoes = [0, 1, 2, 3, 4]
    while operacao not in operacoes:
        print('Operação inválida! Digite uma das seguinte opções: ')
        operacao = int(input('Digite a opção desejada: '))
    return operacao


operacao = menu()
valor_calculado = calculadora(valor_1, valor_2, operacao)
if valor_calculado != None:
    print(f'Resultado: {valor_calculado}')