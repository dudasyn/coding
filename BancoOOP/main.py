from banco import Banco
from cliente import Cliente
from conta import ContaPoupanca, ContaCorrente

bradesco = Banco()
eduardo = Cliente("Eduardo", 36)
santana = Cliente("Santana", 30)
mariopolis = Cliente("Mariopolis", 18)

conta1 = ContaPoupanca(111, 1, 0)
conta2 = ContaPoupanca(222, 2, 0)
conta3 = ContaPoupanca(333, 3, 0)

bradesco.adiciona_cliente(eduardo)
bradesco.inserir_conta(conta1)

bradesco.adiciona_cliente(santana)
bradesco.inserir_conta(conta2)

bradesco.adiciona_cliente(mariopolis)
bradesco.inserir_conta(conta3)

if bradesco.autenticar(eduardo):
    eduardo.conta.depositar(0)
    eduardo.conta.sacar(20)
else:
    print('Cliente não autenticado.')
mariopolis
print('####################')

if bradesco.autenticar(mariopolis):
    mariopolis.conta.depositar(0)
    mariopolis.conta.sacar(20)
else:
    print('Cliente não autenticado.')
