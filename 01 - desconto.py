print('1 - Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de '
      'desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto '
      '(exercício da apostila - aula 2)')

preco = float(input('Digite o preço do produto: '))
p = float(input('Digite o percentual de desconto (0-100)%: '))

desconto = preco * (p / 100)
final = preco - desconto

print('O preço do produto é {}. Desconto de {}%.'.format(preco, p))
print('Valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto, final))