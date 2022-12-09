from Cliente import Cliente
from Conta import Conta
class Teste:

    def test_answer(self):
        cliente = Cliente("jhonny", 83991659350, "084.870.694-36")
        cliente2 = Cliente("Joao", 83991659350, "084.870.694-30")
        conta = Conta(cliente.get_nome(), 5, 20)
        conta2 = Conta(cliente2.get_nome(), 123322, 40)


        assert cliente.set_telefone(83991659354) == cliente.set_telefone(83991659354)
        assert cliente.get_telefone()== 83991659354
        assert conta.get_numero() == 5
        assert conta.get_titular() == "jhonny"
        assert conta.set_numero(10) == conta.set_numero(10)
        assert conta.set_titular("joao") == conta.set_titular("joao")
        assert conta.get_saldo() == 0.0
        assert conta.depositar(100)==conta.set_saldo(100)
        assert conta.get_saldo()==100.0
        assert conta.saque(50) == conta.set_saldo(50)
        assert conta.get_saldo()==50.0
        assert conta.trnasferir(conta2,10) == conta2.set_saldo(10)











