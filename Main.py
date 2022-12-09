from Cliente import Cliente
from Conta import Conta


if __name__ == "__main__":
    cliente = Cliente("Jhonny", 83991659354, "084.870.694-36")
    cliente2 = Cliente("Joao", 83991659350, "084.870.694-30")
    conta = Conta(cliente.get_nome(), 123321, 20)
    conta2 = Conta(cliente2.get_nome(), 123322, 40)

    print(len(cliente.get_nome()))

    print("Nome: ", cliente.get_nome(), " Telefone: ", cliente.get_telefone(), "CPF: ", cliente.get_cpf())
    print("Nome: ", cliente.get_nome(), " Numero da conta: ", conta.get_numero(), " Saldo: ", conta.get_saldo())

    print("\n")

    conta.set_numero(8)
    print("Número da conta alterado com sucesso, o novo numero da conta atulizado é: " ,conta.get_numero() , "\n")

    conta.depositar(600)
    conta.saque(100)
    conta.extrto()

    conta.trnasferir(conta2, 200)

    print("Nome: ", cliente2.get_nome(), " Telefone: ", cliente2.get_telefone(), "CPF: ", cliente2.get_cpf())
    print("Nome: ", cliente2.get_nome(), " Numero da conta: ", conta2.get_numero(), " Saldo: ", conta2.get_saldo())




    
