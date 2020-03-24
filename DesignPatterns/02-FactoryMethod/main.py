'''
Abstrai a factory porque precisaremos de filiais

Factory method é um padrão de criação que permite definir uma interface 
(classe abstrata) para criar objetos mas deixa as subclasses decidirem 
quais objetos criar. O Factory  method permite adiar a instanciação para as subclasses, garatnindo o baixo 
acoplamento entre classes. GO4

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
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()

class ZonaNorteVeiculoFactory(VeiculoFactory):

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

class ZonaSulVeiculoFactory(VeiculoFactory):

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        

        if tipo == 'popular':
            return CarroPopular()

        assert 0, 'Veiculo nao existe'

    def buscar_cliente(self):
        self.carro.buscar_cliente()

if __name__ == "__main__":

    from random import choice

    veiculos_disponiveis_zona_norte = ['luxo','popular','moto']
    veiculos_disponiveis_zona_sul = ['popular']

    for i in range(3):
        carro = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()

    print('XXXX')

    for i in range(4):
        carro = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        carro.buscar_cliente()
