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

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        assert 0, 'Veiculo nao existe'


if __name__ == "__main__":
    from random import choice
    carros_disponiveis = ["luxo","popular","moto"]

    for i in range(12):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_cliente()