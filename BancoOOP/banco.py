class Banco:

    def __init__(self):

        self._agencias = [111,222,333]
        self._clientes = []
        self._contas = []


    def adiciona_cliente(self, cliente):
            
        self._clientes.append(cliente)

    def inserir_conta(self, conta):
        self._contas.append(conta)

    def autenticar(self, cliente):

        if cliente not in self._clientes:
            return False

        if cliente.conta not in self._contas:
            return False

        return True
