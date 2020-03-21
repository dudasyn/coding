from abc import ABC, abstractmethod



class Conta(ABC):

    def __init__(self, agencia, conta, saldo):

        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @abstractmethod
    def sacar(self): pass

    def depositar(self, valor):
        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia} '
                f'Conta: {self.conta} '
                f'Saldo: {self.saldo}')

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo


class ContaPoupanca(Conta):

    def sacar(self, valor):
        if self._saldo  >= valor:
            self._saldo -= valor
        else:
            print('Saldo Insuficiente')
        self.detalhes()


class ContaCorrente(Conta):

    def __init__(self, agencia, conta, saldo, limite = 1000):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    def sacar(self, valor):

        if self._saldo + self._limite >= valor:
            self._saldo -= valor
        else:
            print('Saldo Insuficiente')

        self.detalhes()

cp = ContaPoupanca('ABC','1234',10000)