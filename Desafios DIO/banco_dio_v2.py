import textwrap

def menu():

    menu = '''

    ==========MENU==========

    [1]\tDesposito

    [2]\tSaque

    [3]\tExtrato
    
    [4]\tNova conta
    
    [5]\tListar Contas
    
    [6]\tNovo usuário

    [0]\tSair

    '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):

    if valor > 0:

        saldo += valor
        extrato += f'Deposito: R$ {valor:.2f}\n'
        print('\nDeposito concluido\n')

    else:

        print('Esta operação falhou, o valor é invalido\n')

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if numero_saques < limite_saques:

        if (valor <= limite and valor <= saldo) and valor > 0:

            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print('Saque concluido\n')

        elif valor > saldo:

            print('Esta operação falhou, saldo insuficiente\n')

        elif valor > limite:

            print('Esta operação falhou, o valor execede o limite de saque\n')

        else:

            print('Esta operação falhou, o valor é invalido\n')

    else:

        print('Esta operação falhou, limite de saque diários atingido\n')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):

    print('\n***********EXTRATO**********')
    print('Não foram efetuadas movimentações' if not extrato else extrato)
    print('****************************')
    print(f'Saldo: R$ {saldo:.2f}')
    print('****************************')

def criar_usuario(usuarios):

    cpf = input('Digite seu CPF(somente números): ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:

        print('*** Já existe esse usuário com esse CPF ***')
        return

    nome = input('Informe seu nome completo: ')
    data_nascimento = input('Informe sua data de nascimento(DD-MM-AAAA): ')
    endereco = input('Informe seu endereço (Logaduro, Nº - Bairro - Cidade/UF): ')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print('*** Usuário criado com sucesso ***')

def filtrar_usuarios(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):

    cpf = input('Informe o seu CPF: ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('*** Conta criada com sucesso ***')
        return {"agencia": agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    else:
        print('*** Usuário não encontrado, encerrando a operação ***')

def listar_contas(contas):

    for conta in contas:
        linha = f"""
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """

        print('*' * 30)
        print(textwrap.dedent(linha))


def main():
    agencia = "0001"
    usuarios = []
    contas = []
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    limite_saques = 3

    while True:

        opcao = menu()

        if opcao == '1':

            valor = float(input('\nInforme o valor do deposito: \n'))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':

            valor = float(input('\nInforme o valor do saque: \n'))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = limite_saques
            )


        elif opcao == '3':

            exibir_extrato(saldo, extrato = extrato)

        elif opcao == '4':

            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '5':

            listar_contas(contas)

        elif opcao == '6':

            criar_usuario(usuarios)

        elif opcao == '0':

            break

        else:

            print('Operação invalida, selecione novamente')


main()