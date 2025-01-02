"""Crea una clase abstracta Figura con un método area que deba implementarse en las subclases.
"""
from abc import ABC, abstractmethod #para clases y metodos abstractos

class Figura:
    pass

    @abstractmethod
    def area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

rectangulo1 = Rectangulo(2,10)
print(rectangulo1.area())

        