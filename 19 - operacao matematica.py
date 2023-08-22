print('Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: adição (+), subtração (-), multiplicação (*) ou divisão (/). Exiba na tela o resultado da operação desejada (exercício da apostila - aula 3). Repita até que a opção saída seja escolhida')
print('CALCULADORA')
print(' + Adição ')
print(' - Subração ')
print(' * Multiplicação ')
print(' / Divisão ')
print('Pressione outra tecla para sair')

while True:
    op = input('Qual operação precisa fazer? ')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o primeiro valor: '))
        y = int(input('Digite o segundo valor: '))

    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}'.format(x, y, res))
        continue

    elif (op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}'.format(x, y, res))
        continue

    elif (op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}'.format(x, y, res))
        continue

    elif (op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}'.format(x, y, res))
        continue

    elif (op == 's'):
        break

    else:
        print('Operação inválida.')

print('Encerrando o programa...')

