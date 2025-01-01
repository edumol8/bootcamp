class Vehiculo:
    def __init__(self, nombre, marca, modelo):
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo

class Auto(Vehiculo):
    def __init__(self, nombre, marca, modelo):
        super().__init__(nombre, marca, modelo)

class Moto(Vehiculo):
    def __init__(self, nombre, marca, modelo):
        super().__init__(nombre, marca, modelo)