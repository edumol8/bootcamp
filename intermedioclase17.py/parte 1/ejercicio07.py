"""Crear una clase Animal con un método hablar. Crear subclases como Perro y Gato que implementen el método hablar.
"""

class Animal():
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "jajaja"
    

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def hablar(self):
        return "wuau wuau"

perro1 = Perro("firualis")
print (f"el perro 1 se llama {perro1.nombre} y dice {perro1.hablar()} ")


"""
class Animal():
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self, habla):
        return habla
    

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def hablar(self, habla):
        return super().hablar(habla)

perro1 = Perro("firualis")
print (f"el perro 1 se llama {perro1.nombre} y dice {perro1.hablar("guau")} ")
"""