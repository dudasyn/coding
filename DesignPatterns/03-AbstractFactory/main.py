'''
Abstract Factory é um padrão de criação que fornece uma interface para
criar familias de objetos relacionados ou edpendentes sem especficiar suas
classes concretas. Geralmente Abstract Factory contra com um ou mais
Factory Methods para criar seus objetos

Uma diferença importante entre Factory Method e Abstract Factory
é que o Factory Method usa herança, enquanto que Abstract Factory
usa a composição

Principios: programe para interfaces, não para implementações
Não fere o OPEN CLOSED principle por que reduz os IF's switchs

'''

from abc import ABC, abstractmethod

class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass

class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass



class CarroLuxoZN(VeiculoLuxo):

    def buscar_cliente(self) -> None:
        print('Carro de luxo zn buscando cliente')

class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular zn buscando cliente')

class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular zn buscando cliente')

class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto luxo zn buscando cliente')


class CarroLuxoZS(VeiculoLuxo):

    def buscar_cliente(self) -> None:
        print('Carro de luxo zs buscando cliente')

class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular zs buscando cliente')

class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular zs buscando cliente')

class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto luxo zs buscando cliente')

class VeiculoFactory:

    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo: pass

    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular: pass

    @staticmethod
    @abstractmethod
    def get_moto_luxo() -> VeiculoLuxo: pass
    
    @staticmethod
    @abstractmethod
    def get_moto_popular() -> VeiculoPopular: pass


class ZonaNorteVeiculoFactory(VeiculoFactory):


    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod

    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod

    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZN()
    
    @staticmethod

    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZN()

class ZonaSulVeiculoFactory(VeiculoFactory):

    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod

    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZS()
    
    @staticmethod

    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZS()

class Cliente:

    def buscar_clientes_zn(self):
        for factory in [ZonaNorteVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()


    def buscar_clientes_zs(self):
        for factory in [ZonaSulVeiculoFactory()m ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()



if __name__ == "__main__":
    
    cliente = Cliente()
    cliente.buscar_clientes_zn()
    print()
    cliente = Cliente()
    cliente.buscar_clientes_zs()
