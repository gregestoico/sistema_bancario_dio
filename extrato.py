#formato de visualização: R$xxxx.xx

#operação de extrato :
#   -> deve listar todos os depósitos e saques realizados.
#   -> ao final do extrato, deve-se informar o saldo do usuário.

class Extrato:
    
    def __init__(self):
        self._dicionario = dict()
        

    @property
    def dicionario(self):
        for chave, valor in self._dicionario.items():
            print(f"Operação: {chave} | Valor: R${valor}")

    @dicionario.setter
    def dicionario(self, valor:dict):
        self._dicionario.update(valor)

