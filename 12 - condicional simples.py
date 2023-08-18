print('Traduza as afirmações a seguir para condicionais em python:')
print('a) se idade é maior que 60, escreva: "Você tem direito aos benefícios"')
if(idade > 60):
    print('Você tem direito aos benefícios')

print('b) se dano é maior do que 10 e escudo é igual a 0, escreva: "Você está morto!"')
if(dano > 0 and escudo == 0):
    print('Você está morto!')

print('c) se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em True, escreva: "Você escapou!"')
if(norte == True or sul == True or leste == True or oeste == True):
    print('Você escapou!')


if(norte or sul or leste or oeste):
    print('Você escapou!')