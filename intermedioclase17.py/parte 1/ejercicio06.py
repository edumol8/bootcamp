""""Crear una clase Empleado con atributos nombre y salario. Implementar un método que calcule el salario anual.
"""

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_anual(self):
        return self.salario * 12

empleado1= Empleado("Eduardo", 300)
print(empleado1.calcular_anual())         