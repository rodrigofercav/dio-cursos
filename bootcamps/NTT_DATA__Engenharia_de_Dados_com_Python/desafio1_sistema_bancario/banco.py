import os
from datetime import datetime

LIMITE_QTD_SAQUES = 3
LIMITE_POR_SAQUE = 500

saldo = 0
extrato = ""
qtd_saques = 0
data_ultimo_saque = ""

def data_hora_atual(tipo = "DH"):
    data_hora_atual = datetime.now()
    
    # Apenas Data
    if tipo == "D":
        return data_hora_atual.strftime('%Y-%m-%d')    
    
    # Padrão (DH) = yyyy-mm-dd hh:mm
    return data_hora_atual.strftime('%Y-%m-%d %H:%M')
#

def alimenta_extrato(operacao, valor):
    texto  = f"{data_hora_atual()} -> "
    texto += "Depósito " if operacao == "D" else "Saque    "
    texto += f"-> R${valor:.2f}\n"
    
    return texto
#

def cabecalho(texto, saldo_atual = 0):
    os.system("cls") if os.name == "nt" else os.system("clear")
    print(".----------------------------.")
    print(f"| {" Banco Python ".center(26, "*")} |")
    print(f"| {(f" {'-'.join(texto)} ").center(26)} |")
    print("`----------------------------´\n")
    
    #if texto != 'MENU':
    print(f"Saldo Atual: R${saldo_atual:.2f}\n")
#

def pressione_enter():
    input("\nPressione [ENTER] para voltar ao menu.")
#


#start
while True:
    cabecalho("MENU", saldo)
    print(" [D] Depositar")
    print(" [E] Extrato")
    print(" [S] Sacar\n")
    print(" [X] Sair\n")
    
    opcao_menu = input(">>> ")
    opcao_menu = opcao_menu.upper()
    
    # -------------------
    # operações bancárias
    # -------------------
    if opcao_menu == "D":
        cabecalho("DEPOSITAR", saldo)
        valor_deposito = input("Valor do depósito: ")
        valor_deposito = 0 if valor_deposito == '' else float(valor_deposito)
        
        if valor_deposito <= 0:
            print("\nValor inválido! \nVocê deve informar um valor maior que 0 (zero).")
            
        else:
            saldo += valor_deposito
            extrato += alimenta_extrato(opcao_menu, valor_deposito)
            
            print(f"\nSaldo foi atualizado para R${saldo:.2f}")
        #
    elif opcao_menu == "E":
        cabecalho("EXTRATO", saldo)
        print(extrato if extrato != "" else "Não há histórico de operações.\n", end='')
        #
    elif opcao_menu == "S":
        cabecalho("SACAR", saldo)
        
        if not qtd_saques < LIMITE_QTD_SAQUES:
            print(f"Operação não permitida! \nVocê já utilizou a quantidade de {LIMITE_QTD_SAQUES} saque(s) diário(s).")
        
        elif saldo == 0:
            print("Operação não permitida! \nVocê deve ter saldo maior que 0 (zero).")
        
        else:
            valor_saque = input("Valor do Saque: ")
            valor_saque = 0 if valor_saque == '' else float(valor_saque)
                        
            if valor_saque <= 0:
                print("\nValor inválido! \nVocê deve informar um valor maior que 0 (zero).")
                
            elif valor_saque > LIMITE_POR_SAQUE:
                print(f"\nOperação não permitida! \nSeu limite é de R${LIMITE_POR_SAQUE:.2f} por saque.")
                
            elif saldo < valor_saque:
                print(f"\nOperação falhou! \nVocê não tem saldo para realizar o saque.")
                
            else:
                # valida limites diarios 
                if data_ultimo_saque == "":
                    data_ultimo_saque = data_hora_atual("D")
                
                if data_ultimo_saque == data_hora_atual("D"):
                    qtd_saques += 1
                else:
                    qtd_saques = 1
                
                # atualiza saldo e histórico do extrato
                saldo -= valor_saque
                extrato += alimenta_extrato(opcao_menu, valor_saque)
                
                print(f"\nSaldo foi atualizado para R${saldo:.2f}")
            #
        #
    elif opcao_menu == "X":
        print("Saindo do aplicativo...")
        break
        #
    else:
        print("\nOpção inválida, tente novamente.")
    #
    
    pressione_enter()
#fim-while-menu
