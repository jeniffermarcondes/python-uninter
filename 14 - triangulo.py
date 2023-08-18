print('Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como:')
print('a) Equilátero (três lados iguais)')
print('a) Isósceles (dois lados iguais)')
print('a) Escaleno (três lados diferentes)')

print('Lembre-se de que, para formar um triângulo, nenhum dos lados pode ser igual a zero, e um lado não pode ser maior do que a soma dos outros dois (exercício da apostila - aula 3) ')

A = int(input('Digite o 1º lado do triângulo:'))
B = int(input('Digite o 2º lado do triângulo:'))
C = int(input('Digite o 3º lado do triângulo:'))

if (A > 0 )and (B > 0) and (C > 0):
    if (A + B > C) and (A + C > B) and (B +C > A):
    # se você chegou até aqui, é porque o triangulo é válido!
        if A != B and A != C and B != C:
            print('Triângulo escaleno!')
        else:
            if A == B and A == C and B == C:
                print('Triângulo equilátero!')
            else:
                print('Triângulo isósceles')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo')

else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo')


