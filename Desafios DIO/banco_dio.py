menu = '''

Selecione um opção:

[1] = Desposito

[2] = Saque

[3] = Extrato

[0] = Sair

'''

saldo = 0
LIMITE = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':

        valor = float(input('\nInforme o valor do deposito: '))

        if valor > 0:

            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
            print('Deposito concluido\n')

        else:

            print('Esta operação falhou, o valor é invalido\n')

    elif opcao == '2':

        valor = float(input('\nInforme o valor do saque: '))

        if numero_saques < LIMITE_SAQUES:

            if (valor <= LIMITE and valor <= saldo) and valor > 0:

                saldo -= valor
                extrato += f'Saque: R$ {valor:.2f}\n'
                numero_saques += 1
                print('Saque concluido\n')

            elif valor > saldo:

                print('Esta operação falhou, saldo insuficiente\n')

            elif valor > LIMITE:

                print('Esta operação falhou, o valor execede o limite de saque\n')

            else:

                print('Esta operação falhou, o valor é invalido\n')

        else:

            print('Esta operação falhou, limite de saque diários atingido\n')

    elif opcao == '3':

        print('\n***********EXTRATO**********')
        print('Não foram efetuadas movimentações' if not extrato else extrato)
        print('****************************')
        print(f'Saldo: R$ {saldo:.2f}')
        print('****************************')

    elif opcao == '0':

        break

    else:

        print('Operação invalida, selecione novamente')