from abc import ABC, ABCMeta, abstractclassmethod, abstractproperty
from datetime import datetime
import textwrap


class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = 0
        self._numero = numero
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
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._histórico
    
    
    def sacar(self, valor, saldo):
        self.saldo = saldo
        excedeu_saldo = valor > excedeu_saldo
        
        if excedeu_saldo:
            print("!!!!! Operação Falhou! Saldo Insuficiente")
            
        elif valor > 0:
            self._saldo -= valor
            print(f"Saque de R$ {valor} realizado om sucesso!!")
            return True
        
        else:
            print("VALOR INFORMADO INVÁLIDO!!!")
        
        return False
        
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"!!! Depósito de R$ {valor} realizado com Sucesso!")
            
        else:
            print("!!! VALOR INFORMADO INVÁLIDO")
        

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saque = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque
        
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        excedeu_limite = valor > self.limite
        excedeu_saque = numero_saques >= self.limite_saques
        
        if excedeu_limite:
            print("!!! O Valor Excede o limite !!!")
            
        elif excedeu_saque:
            print("!!! Número de Saques Excedido !!!")
            
        else:
            return super().sacar(valor)
        
        
    def __str__(self):
        return f"""\
            Agência: \t{self.agencia}
            C/C: \t{self.numero}
            Titular: \t{self.cliente.nome}
            """
        

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        

class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass        
    
    @abstractclassmethod
    def registrar(self, conta):
        pass
    

class Deposito:
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime
                ("%d-%m-%Y %H:%M:%s"),
            }
        )
        
        
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n!!! CLIENTE SEM CONTA !!!!")
        return 
    
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    
    if not cliente:
        print("!!! CLIENTE NÃO ENCONTRADO !!!")
        return
    
    valor = float(input("Informe o valor do Depósito"))
    transacao = Deposito(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)
    
    
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    
    if not cliente:
        print("!!! CLIENTE NÃO ENCONTRADO !!!")
        return
    
    valor = float(input("Informe o valor do Saque"))
    transacao = Saque(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    
    if not cliente:
        print("!!! CLIENTE NÃO ENCONTRADO !!!")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n\n ----------EXTRATO----------")
    transacoes = conta.historico.transacoes
    
    extrato = ""
    if not transacoes:
        extrato = "Não encontramos movimentações em sua conta"
    
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"
            
    print(extrato)
    print(f"\nSaldo:\n\tR${conta.saldo:.2f}")


def criar_clientes(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    
    if cliente:
        print("!!! CLIENTE JÁ CADASTRADO !!!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd--mm-aaaa): ")
    endereco = input("Informe o endereço: ")
    
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    
    clientes.append(cliente)
    
    print("\n *** CLIENTE CADASTRADO COM SUCESSO ***")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    
    if not cliente:
        print("!!! CLIENTE NÃO ENCONTRADO !!!")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    clientes.contas.append(conta)
    
    print("\n *** CONTA CRIADA COM SUCESSO ***")


def listar_conta(contas):
    for conta in contas:
        print("-" + 100)
        print(textwrap.dedent(str(conta)))

            
def main():
    clientes = []
    contas = []
    
    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes) 

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_clientes(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(numero_conta, clientes, conta)

        elif opcao == "lc":
            listar_conta(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
            
main()
