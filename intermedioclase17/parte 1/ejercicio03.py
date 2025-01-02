"""Crear una clase Rectángulo con atributos base y altura. Implementar un método que determine si es un cuadrado.
"""


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def es_cuadrado(self):
        return self.base == self.altura 
    
rectangulo1 = Rectangulo(5, 5)
print(rectangulo1.es_cuadrado())

rectangulo2 = Rectangulo(4, 9)
print(rectangulo2.es_cuadrado())
