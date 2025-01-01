"""Implementa una clase Vehiculo con un contador de instancias.
"""

class Vehiculo:
    contador = 0

    def __init__(self, marca, modelo):
        Vehiculo.contador += 1
        self.marca = marca 
        self.modelo = modelo


carro = Vehiculo("Ford", "mustang")
carro = Vehiculo("Mercedes", "benzs")
carro = Vehiculo("Mazda", "3")


print(Vehiculo.contador)

