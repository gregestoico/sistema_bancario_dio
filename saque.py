#formato de visualização: R$xxxx.xx

#operação de saque :
#   -> permite no máximo 3 saques diários, limitados a R$500 reais por saque.
#   -> caso o saldo seja insuficiente, o saque é cancelado e uma mensagem para o usuário informando que "é impossível sacar o dinheiro. por falta de saldo" deve ser exibida.
#   -> devem ser armazenados em uma variável e exibidos na operação extrato.

class Saque:
    quantidade_saques = 3

    #retorna o valor do saldo após a operação.
    def realizar_saque(self, valor_saldo, valor_saque):

        if self.quantidade_saques == 0:
            print("Impossível realizar o saque: quantidade de saques diários esgotados.")
            return valor_saldo
         
        elif valor_saque <= 0:
            print("Ímpossível realizar o saque: valor inválido.")
            return valor_saldo


        elif valor_saque > valor_saldo:
            print("Impossível realizar o saque: falta de saldo.")
            return valor_saldo
        
        elif valor_saque > float(500):
            print("Impossível realizar o saque: o limite para saques é de: R$500.00")
            return valor_saldo
        
        else:
            print("Saque realizado com sucesso!!")
            self.quantidade_saques -= 1
            return valor_saldo - valor_saque, valor_saque
            