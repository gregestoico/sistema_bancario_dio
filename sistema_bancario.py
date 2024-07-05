#sistema com apenas um usuário

import extrato
import saque
import deposito
import random

valor_saldo = float()

instancia_deposito = deposito.Deposito()
instancia_saque = saque.Saque()
instancia_extrato = extrato.Extrato()

print("Seja bem vindo ao menu do banco!")
opcao = int(1)
while(opcao != 0):
    opcao = int(input("Digite 1 para realizar depósito, 2 para saque, 3 para extrato e 0 para sair: "))
    if opcao == 1:
        numero_operacao = random.randint(0,9999)
        valor_saldo, input_recebido = instancia_deposito.realizar_deposito(valor_saldo, float(input("Digite o valor a ser depositado: R$")))
        instancia_extrato.dicionario = {f'Deposito nº{numero_operacao}':input_recebido,}        

    elif opcao == 2:
        numero_operacao = random.randint(0,9999)
        valor_saldo, input_recebido = instancia_saque.realizar_saque(valor_saldo, float(input("Digite o valor a ser sacado: R$")))
        instancia_extrato.dicionario = {f'Saque nº{numero_operacao}': input_recebido,}

    elif opcao == 3:
        instancia_extrato.dicionario
        print(f"Saldo de: R${valor_saldo}")


