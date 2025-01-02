"""Crear una clase Fracción con atributos numerador y denominador. Implementar un método para sumar dos fracciones.
"""

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def sumar(self, otra):
        nuevo_num = self.numerador * otra.denominador + otra.numerador * self.denominador
        nuevo_den = self.denominador * otra.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def dividir(self, nueva):
        num_div = self.numerador * nueva.denominador
        den_div = self.denominador * nueva.numerador
        return Fraccion(num_div, den_div)

    def __str__(self):
      return f"{self.numerador}/{self.denominador}"

fraccion1 = Fraccion(2,3)
fraccion2 = Fraccion(5,4)
print(fraccion1.dividir(fraccion2))