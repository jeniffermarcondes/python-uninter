#Início da função cachorro_peso()
def cachorro_peso():

  while True:
    try:
      peso = int(input('Entre com o peso do cachorro: '))
      if (peso < 3):
        return + 40
      elif (peso >= 3) and (peso < 10):
        return + 50
      elif (peso >= 10) and (peso < 30):
        return + 60
      elif (peso >= 30) and (peso < 50):
        return + 70
      else:
        print('Não aceitamos cachorros tão grandes. \n'
              'Por favor entre com o peso do cachorro novamente. \n')
        continue # retorna para pergunta
    except ValueError: #caso o usuário digite letra ou número quebrado (500.50)
      print('Você digitou um valor não numérico \n'
            'Por favor entre com o peso do cachorro novamente \n')
#Fim da função cachorro_peso()

#Início da função cachorro_pelo()
def cachorro_pelo():

  while True:
    pelo = input('Entre com o pelo do cachorro \n'+
                    'c - Pelo curto \n'+
                    'm - Pelo médio \n'+
                    'l - Pelo Longo \n'+
                    '>> ')
    pelo = pelo.lower()
    pelo = pelo.strip()
    if pelo == 'c':
      return 1
    elif pelo == 'm':
      return 1.5
    elif pelo == 'l':
      return 2
    else:
      print('Pare de digitar opções diferentes de c/m/l \n')
      continue # voltar para o início
#Fim da função cachorro_pelo()

#Início da função cachorro_extra()
def cachorro_extra():

  acumulador = 0
  while True:
    extra = input('Deseja adicionar mais algum serviço? \n'+
                            '1 - Corte de Unhas - R$ 10,00 \n'+
                            '2 - Escovar Dentes - R$ 12,00 \n'+
                            '3 - Limpeza de Orelhas - R$ 15,00 \n'+
                            '0 - Não desejo mais nada \n' +
                            '>> ')
    if extra == '0':
      return acumulador
    elif extra == '1':
      acumulador = acumulador + 10
      continue
    elif extra == '2':
      acumulador = acumulador + 12
      continue
    elif extra == '3':
      acumulador = acumulador + 15
      continue
    else:
      print('Pare de digitar opções diferentes de 0/1/2/3!')

#Fim da função cachorro_extra()

#Início do Main
print('---------- Bem-vindo ao pet shop da Jeniffer Marcondes das Almas ----------')
peso = cachorro_peso()
pelo = cachorro_pelo()
extra = cachorro_extra()
total = (peso * pelo) + extra
print('Total a pagar(R$): {:.2f} (peso: {} * pelo: {} + adicional(is): {})'.format(total,peso,pelo,extra))
