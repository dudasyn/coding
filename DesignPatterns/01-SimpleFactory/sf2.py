'''
Nesse caso o cliente vai usar a própria factory para o utilziar 
o produto dentro dela
'''

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: 
        pass

class CarroLuxo(Veiculo):

    def buscar_cliente(self) -> None:
        print('Carro de luxo buscando cliente')

class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular buscando cliente')

class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto buscando cliente')

class VeiculoFactory:

    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        assert 0, 'Veiculo nao existe'

    def buscar_cliente(self):
        self.carro.buscar_cliente()

if __name__ == "__main__":

    from random import choice
    carros_disponiveis = ['luxo','popular','moto']

    for i in range(12):
        carro = VeiculoFactory(choice(carros_disponiveis))
        carro.buscar_cliente()