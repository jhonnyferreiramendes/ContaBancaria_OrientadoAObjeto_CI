class Conta:
    def __init__(self, titular, numero, saldo):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = 0.0

    def saque(self, valor):
        if(self.__saldo >= valor):
            self.__saldo -= valor
            print("Saque realizado com sucesso no valor de: ", valor)
            print("Valor atual do saldo: ", self.__saldo, "\n")
        else:
            print("Saldo insuficiente \n")

    def depositar(self, valor):
        self.__saldo += valor
        print("deposito realizado com sucesso no valor de: ", valor)
        print("Valor atual do saldo: ", self.__saldo, "\n")

    def trnasferir(self, conta_destino, valor):
        if self.__saldo < valor:
            print("Impossivel fazer trasnferencia, saldo insuficiente! \n")
        else:
            self.saque(valor)
            conta_destino.depositar(valor)




    def extrto(self):
        print("Cliente: ", self.__titular, "Saldo atual: ", self.__saldo, "\n")



    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero


    def get_saldo(self):
        return self.__saldo


    def set_saldo(self, saldo):
        if(saldo < 0):
            print("Saldo nao pode ser negativo")
        else:
            self.__saldo = saldo





