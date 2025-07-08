print("==SISTEMA BANCÁRIO==")

menu = """ 

    1 - Depositar
    2 - Sacar
    3 - Ver extrato
    0 - Sair

"""

saldo = 0.0
limite = 500.0
LIMITE_SAQUE = 3
extrato = ""
num_saques = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        valor = float(input("Valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Falha na operação! Informe umm valor válido")

    elif opcao == "2":
        print("Saque")
        saque = float(input("Valor a ser sacado: "))
       
        if saque > saldo:
            print("Erro: saldo insuficiente!")
        elif saque > limite:
            print(f"Erro: o saque ultrapassa o valor limite de R${limite:.2f}")
        elif num_saques >= 3:
            print("Erro: limite de saques diários atingido")
        
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            num_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Falha na operação! Informe umm valor válido")
    elif opcao == "3":
        print("=========EXTRATO=========")
        print("Nenhuma operação realizada." if not extrato else extrato)
        print(f"\nSaldo atual: R${saldo:.2f}\n")
        print("=========================")
    elif opcao == "0":
        break
    else:
        print("Erro! Informe uma operação válida.")