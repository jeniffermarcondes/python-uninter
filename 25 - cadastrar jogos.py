print('Suponha que você é um colecionador de jogos de videogame. Escreva um algoritmo que permita cadastrar esses jogos informando o nome e a qual videogame ele pertente')
print('Para isso, crie um menu de opções contendo: cadastrar novo item, listar tudo que foi cadastrado e sair')
print('Para resolver esse exercício, crie pelo menos uma função para cada item do menu')
print('Além disso, armazene todos os dados em um arquivo de texto que deve ser salvo em disco e manter os dados cadastrados')

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+') # w - escrita | t - txt | + caso não exista cria o arquivo
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt') # r - leitura | t - txt
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at') # a - abrir para escrita mas preserva o conteúdo se já existir | t - txt
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomeJogo,nomeVideogame))
    finally:
        a.close()

#Programa principal

arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ',1,3)
    if op == 1:
        print('Opção de cadastrar novo item selecionada...\n')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif op == 2:
        print('Opção de listar selecionada...\n')
        listarArquivo(arquivo)

    elif op == 3:
        print('Encerrando o programa...')
        break