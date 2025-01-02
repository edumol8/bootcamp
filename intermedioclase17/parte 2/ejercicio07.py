"""Crea una clase Empleado y una subclase Gerente que utilice super() para llamar al constructor de la clase base.
"""

class Empleado:
    def __init__(self, nombre, cedula, cargo):
        self.nombre = nombre
        self.cedula = cedula
        self.cargo = cargo

class Gerente(Empleado):
    def __init__(self, nombre, cedula, cargo, area):
        super().__init__(nombre, cedula, cargo)
        self.area = area
    