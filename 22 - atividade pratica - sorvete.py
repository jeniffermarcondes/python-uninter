print('Bem-vindo a Sorveteria da Jeniffer Marcondes das Almas')
print('')
print('-' * 38 + 'CARDÁPIO' + '-' * 38)
print('| Nº DE BOLAS | SABOR TRADICIONAL (tr)  | SABOR PREMIUM (pr) | SABOR ESPECIAL (es) |')
print('|           1 |                R$ 6,00  |           R$ 7,00  |            R$ 8,00  |')
print('|           2 |                R$ 10,00 |           R$ 12,00 |            R$ 14,00 |')
print('|           3 |                R$ 14,00 |           R$ 17,00 |            R$ 20,00 |')
print('-' * 84)

acumulador = 0

while True:
    sabor = input('Entre com o sabor desejado (tr/pr/es): ')
    sabor = sabor
    if sabor != 'tr' and sabor != 'es' and sabor != 'pr':
        print('Sabor inválido. Tente novamente')
        continue  # se o usuário digitar algo inválido volta para o começo do while

    qtd_bolas = input('Entre com o número de bolas de sorvete desejado (1/2/3): ')
    if qtd_bolas != '1' and qtd_bolas != '2' and qtd_bolas != '3':
        print('Número de bolas de sorvete inválido. Tente novamente')
        continue

    if sabor == 'tr' and qtd_bolas == '1':
        print('Você pediu 1 bola de sorvete no sabor TRADICIONAL: R$ 6,00')
        acumulador = acumulador + 6  # pega o valor que tinha no acumulador e soma com 6

    elif sabor == 'tr' and qtd_bolas == '2':
        print('Você pediu 2 bolas de sorvete no sabor TRADICIONAL: R$ 10,00')
        acumulador = acumulador + 10

    elif sabor == 'tr' and qtd_bolas == '3':
        print('Você pediu 3 bolas de sorvete no sabor TRADICIONAL: R$ 14,00')
        acumulador = acumulador + 14

    elif sabor == 'pr' and qtd_bolas == '1':
        print('Você pediu 1 bola de sorvete no sabor PREMIUM: R$ 7,00')
        acumulador = acumulador + 7

    elif sabor == 'pr' and qtd_bolas == '2':
        print('Você pediu 2 bolas de sorvete no sabor PREMIUM: R$ 12,00')
        acumulador = acumulador + 12

    elif sabor == 'pr' and qtd_bolas == '3':
        print('Você pediu 3 bolas de sorvete no sabor PREMIUM: R$ 17,00')
        acumulador = acumulador + 17

    elif sabor == 'es' and qtd_bolas == '1':
        print('Você pediu 1 bola de sorvete no sabor ESPECIAL: R$ 8,00')
        acumulador = acumulador + 8

    elif sabor == 'es' and qtd_bolas == '2':
        print('Você pediu 2 bolas de sorvete no sabor ESPECIAL: R$ 14,00')
        acumulador = acumulador + 14

    elif sabor == 'es' and qtd_bolas == '3':
        print('Você pediu 3 bolas de sorvete no sabor ESPECIAL: R$ 20,00')
        acumulador = acumulador + 20

    pedir_mais = input(' Deseja mais algum sorvete (s/digite ou tecla)?: ')
    pedir_mais = pedir_mais.upper()  # resolvo o problema digitar s e S ou n e N
    if pedir_mais == 'S':
        continue
    else:
        print('O valor total a ser pago: R$ {:.2f}'.format(acumulador))
        break
