"""Crea una clase Matematica con un método estático que calcule el área de un círculo dado el radio.
"""
import math as m

class Matematica:
    @staticmethod
    def area_circulo(radio):
        return m.pi * (radio**2)

areacirculo = Matematica.area_circulo(5)
print(areacirculo)