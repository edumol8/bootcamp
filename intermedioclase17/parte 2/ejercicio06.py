"""Implementa una clase base Animal con un método hablar. Crea una subclase Perro que sobrescriba este método.
"""

class Animal:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
    
    def hablar(self):
        return("animal habla")
    
class Perro(Animal):
    def __init__(self, nombre, peso):
        super().__init__(nombre, peso)
    
    def hablar(self):
        return ("guau guau")
    

animal1 = Animal("Paco", "45kg")
print(animal1.hablar())

perro1 = Perro("Firulais", "4kg")
print(perro1.hablar())

