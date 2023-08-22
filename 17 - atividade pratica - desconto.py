print('Bem vindo(a) a loja da Jeniffer Marcondes das Almas')
valor_produto = float(input('Entre com o valor do produto: '))
qtd_produto = int (input('Entre com a quantidade desejada: '))
desconto_produto = 0
if qtd_produto < 200:
  desconto_produto = 0.00
elif 200 <= qtd_produto < 1000:
  desconto_produto = 0.05 # 5% = 0.05 || 100% = 1.00
elif 1000 <= qtd_produto < 2000:
  desconto_produto = 0.10 # 10% = 0.10 || 100% = 1.00
else:
  desconto_produto = 0.15 # 15% = 0.15 || 100% = 1.00

total_sem_desconto = valor_produto * qtd_produto
print('O valor total SEM desconto é de: R$ {:.2f}'.format(total_sem_desconto))
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
print('O valor total COM desconto é de: R$ {:.2f}'.format(total_com_desconto))