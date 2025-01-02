"""Crear una clase Círculo con un atributo radio. Implementar métodos para calcular el área y el perímetro.
"""
import math 

class Circulo():
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return (self.radio * self.radio) * 3.1416
    
    def calcular_perimetro(self):
        return self.radio * 2 * math.pi
    

    
ciruclo1 = Circulo(5)
print(ciruclo1.calcular_area(), ciruclo1.calcular_perimetro())



