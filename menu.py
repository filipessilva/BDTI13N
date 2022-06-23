import operacoes
import this
this.opcao = -1


def menu():
    print('\n Escolha uma das opções abaixo: \n\n'+
          '1. Cadastrar\n'+
          '2. Consultar\n'+
          '0. Sair')
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):

        menu()

        if this.opcao == 0:
            print ('Obrigado!')

        elif this.opcao == 1:
            print('Informe seu nome:')
            nome = input()
            print('Informe seu telefone:')
            telefone = input()
            print ('Informe seu endereço:')
            endereco = input()
            print('Informar sua data de nascimento: ')
            dtNasc = input()
            #Chamar o metodo inserir
            operacoes.inserir(nome,telefone,endereco,dtNasc)

        elif this.opcao == 2:
            operacoes.consultar()


        else:
            print('Opção escolhida não é valida!')