#formato de visualização: R$xxxx.xx

#operação de depósito :
#   -> recebe valores positivos.
#   -> devem ser armazenados em uma variável e exibidos na operação extrato.

class Deposito:
    #retorna o valor do saldo após a operação.
    def realizar_deposito(self, valor_saldo, valor_deposito):
        if valor_deposito <= 0:
            print("Impossível realizar o depósito: valor negativo ou nulo não é aceito.")
        else:
            return valor_saldo + valor_deposito, valor_deposito