# Curso Python DIO Vivo
# Desafio 1 (Básico): Mini Sistema bancário com 3 operações de Depósito, Saque e Extrato.

menu = """

Selecione uma operação:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("*** Depósito realizado! ***")

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"{numero_saques} Saque: R$ {valor:.2f}\n"
            print("*** Saque realizado! ***")
            
        
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "e":
        print("\n============== EXTRATO ==============")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=======================================")
    
    elif opcao == "q":
        print("*** Sistema finalizado! ***\n")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
