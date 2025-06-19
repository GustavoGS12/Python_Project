import textwrap
from datetime import datetime
from abc import ABC, abstractclassmethod, abstractproperty#, abstractmethod


class Cliente:

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_trasferencia(self, conta, transacao):
        transacao.registrar_transacao(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):

    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:

    def __init__(self, numero_conta , cliente):
        self._saldo = 0
        self._numero_conta = numero_conta
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):

        saldo = self._saldo
        execedeu_saldo = valor > saldo

        if execedeu_saldo:

            print('Esta operação falhou, saldo insuficiente\n')

        elif valor > 0:

            self._saldo -= valor
            print('Saque concluido\n')
            return True

        else:

            print('Esta operação falhou, o valor é invalido\n')

        return False

    def depositar(self, valor):

        if valor > 0:

            self._saldo += valor
            #extrato += f'Deposito: R$ {valor:.2f}\n'
            print('\nDeposito concluido\n')

        else:

            print('Esta operação falhou, o valor é invalido\n')
            return False

        return True, #extrato

class ContaCorrente(Conta):

    def __init__(self, numero_conta, cliente, limite = 500, limite_saque = 3):
        super().__init__(numero_conta, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.limite_saque

        if excedeu_limite:

            print('Esta operação falhou, o valor execede o limite de saque\n')

        elif excedeu_saques:

            print('Esta operação falhou, limite de saque diários atingido\n')

        else:

            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""
        Agência:\t{self.agencia}
        C/C:\t\t{self.numero_conta}
        Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo" : transacao.__class__.__name__,
            "valoe" : transacao.valor,
            "data" : datetime.now().strftime("%d-%m-%Y %H:%M:%s")
        })

class Transacao(ABC):

    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar_transacao(self, conta):
        pass

class Deposito(Transacao):

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar_transacao(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar_transacao(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu():
    inicio = '''

    ==========MENU==========

    [1]\tDesposito

    [2]\tSaque

    [3]\tExtrato

    [4]\tNova conta

    [5]\tListar Contas

    [6]\tNovo usuário

    [0]\tSair

    '''
    return input(textwrap.dedent(inicio))

def filtrar_clientes(cpf, clientes):

    clientes_filtrados = [usuario for usuario in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cleinte(cliente):

    if not cliente.contas:

        print("\nCliente não possui conta!")
        return
    
    #FIXME: Não permite cliente escolher conta

    return cliente.contas[0]

def depositar(clientes):

    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("Cleinte não encontrado...")
        return
    
    valor = float(input("Informe o valor do desposito:"))
    trasacao = Deposito(valor)

    conta = recuperar_conta_cleinte(cliente)

    if not conta:
        return
    
    cliente.realizar_trasferencia(conta, trasacao) 

def sacar(clientes):

    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("Cleinte não encontrado...")
        return
    
    valor = float(input("Informe o valor do saque:"))
    trasacao = Saque(valor)

    conta = recuperar_conta_cleinte(cliente)

    if not conta:
        return
    
    cliente.realizar_trasferencia(conta, trasacao)

def exibir_extrato(clientes):

    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("Cleinte não encontrado...")
        return
    
    conta = recuperar_conta_cleinte(cliente):

    if not conta:
        return
    
    print("==========EXTRATO=========")
    transacoes = conta.historico.transacoes

    extrato - ""
    if not transacoes:

        extrato = "Não foram realizadas movimentações\n"
    else:
        for transacao in transacoes:
            extrato += f"{transacao['tipo']} - R$ {transacao['valor']:.2f}\n"

    print(extrato)
    print(f"Saldo: \n\tR$ {conta.saldo:.2f}")
    print("=========================")  

def criar_usuario(usuarios):

    cpf = input('Digite seu CPF(somente números): ')
    usuario = filtrar_clientes(cpf, usuarios)

    if usuario:

        print('*** Já existe esse usuário com esse CPF ***')
        return

    nome = input('Informe seu nome completo: ')
    data_nascimento = input('Informe sua data de nascimento(DD-MM-AAAA): ')
    endereco = input('Informe seu endereço (Logaduro, Nº - Bairro - Cidade/UF): ')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print('*** Usuário criado com sucesso ***')
    
def criar_conta(agencia, numero_conta, usuarios):

    cpf = input('Informe o seu CPF: ')
    usuario = filtrar_clientes(cpf, usuarios)

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
    clientes = []
    contas = []

    while True:

        opcao = menu()

        if opcao == '1':

            depositar(clientes)

        elif opcao == '2':

            sacar(clientes)

        elif opcao == '3':

            exibir_extrato(clientes)

        elif opcao == '4':

            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == '5':

            listar_contas(contas)

        elif opcao == '6':

            criar_usuario(clientes)

        elif opcao == '0':

            break

        else:

            print('Operação invalida, selecione novamente')

main()