menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha uma opção acima: 
'''

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do Depósito:  "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f} realizado\n\n"
            
        else:
            print("Operação falhou, escolha um valor válido")
            
    elif opcao == "s":
        valor = float(input("Informe o valor do Saque:  "))
        
        excedeu_saldo =  valor > saldo
        
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
            extrato += f"Saque de R$ {valor:.2f} realizado\n\n" 
            numero_saque += 1
            
        else:
            print("Operação falhou, escolha um valor válido")
        
    elif opcao == "e":
        nome = "EXTRATO"
        print(nome.center(20, "-"))
        print("\n\nAinda não foram encontradas movimentações" if not extrato else extrato)
        print(f"\n\nSeu saldo é R$ {saldo:.2f}")
        
    elif opcao == "q":
        print("Finalizando atendimento...")
        break
    
    else:
        print("Digite uma opção válida")
