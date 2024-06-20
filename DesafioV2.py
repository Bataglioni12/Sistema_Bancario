from datetime import datetime, date
import textwrap





def menu():
    menu = """\n
    ================ INICIO ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [u]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))





def deposito (saldo, valor, extrato, data, /):
    
    valor = float(input("Digite o valor a ser depositado: \n"))
    
    if valor > 0:
        saldo += valor
        extrato += f"Deposito de RS {valor} realizado em {data}"
        print("Deposito Realizado...")
        
    else:
        print("Depósito falhou. Por favor, deposite um valor válido.")
              
    return saldo, extrato
        
    
    
def saque (*, saldo, valor, extrato, limite, numero_saque, limite_saques, LIMITE_SAQUE, data):
    
    valor = float(input("Digite o valor que deseja sacar"))
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque > LIMITE_SAQUE
    
    if excedeu_saldo:
        print(f"Saldo insuficiente para o valor de {valor:.2f} escolhido")
                   
    elif excedeu_limite:
        print(f"O valor de {valor:.2f} excede o limite permitido, tente outro valor")
            
    elif excedeu_saque:
        print("Você alcancou o limite máximo de saque")
            
    elif  valor > 0:
        saldo -= valor
        extrato += f"Saque de R$ {valor:.2f} realizado\n\n em {data}" 
        numero_saque += 1
        print("Saque realizado...")
            
    else:
        print("Operação falhou, escolha um valor válido")
            
    return saldo, extrato
    
            
def extrato(saldo, /, *, extrato):
    
    nome = "EXTRATO"
    print(nome.center(20, "-"))
    if not extrato:
        print("\n\nAinda não foram encontradas movimentações")
            
    else:     
        print(f"\n\nSeu saldo é R$ {saldo:.2f}")
        
    
def usuario(usuarios, **end):
    
    user = validar_usuario(cpf, usuarios)
    
    if user:
        print(f"o {cpf} já está cadastrado")
        return
    
    nome = input("Digite seu nome: \n")
    dt_nasc =datetime(input("Informe sua data de nascimento: \n"))
    cpf = int(input("Informe seu cpf: \n"))
    end.logradouro = input("Qual seu logradouro?\n")
    end.nro = input("Qual o número da sua casa?\n")
    end.bairo = input("Qual seu bairro?\n")
    end.cidade = input("Qual sua cidade?\n")
    end.estado = input("Qual seu estado?\n")
    
    usuarios.append({"nome" : nome, "cpf" : cpf, "Data de Nascimento" : dt_nasc, "Endereço" : end})
    
def validar_usuario(cpf, usuarios):
    
    filtro_usuario = ""
    for user in usuarios:
        if usuarios["cpf"] == cpf:
            return filtro_usuario [0]
        else:
            filtro_usuario = None
    
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = validar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n!!!!!!! Usuário não encontrado, fluxo de criação de conta encerrado! !!!!!!!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
    
def main():

    saldo = 0
    limite = 500
    numero_saque = 0
    LIMITE_SAQUE = 3
    data = date.today()
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            deposito(saldo, extrato=extrato)
            
        elif opcao == "s":
            saque(saldo, extrato=extrato)
            
        elif opcao == "e":
            extrato(saldo, extrato=extrato)
            
        elif opcao == "u":
            usuario(usuarios = usuario)
            
        elif opcao == "nc":
            numero_conta = len(criar_conta.contas) + 1
            conta = criar_conta(conta.AGENCIA, numero_conta, conta.usuario)

            if conta:
                criar_conta.contas.append(conta)
            
        elif opcao == "lc":
            listar_contas(listar_contas.contas)

        else:
            break
        
main()
