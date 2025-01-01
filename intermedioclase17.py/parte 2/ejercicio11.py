"""Crea una clase Rectangulo que calcule su área como una propiedad.
"""

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    @property
    def calcular_area(self):
        return self.base * self.altura

rectangulo1 = Rectangulo(5, 10)
print(rectangulo1.calcular_area)

