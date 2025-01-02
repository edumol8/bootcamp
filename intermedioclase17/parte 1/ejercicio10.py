"""Crear una clase Libro que contenga un atributo autores como una lista. Implementar un método para agregar y listar los autores.
"""
class Libro:
    def __init__(self, autores):
        self.autores = []
    
    def agregar_autor(self, nuevo_autor):
        self.autores.append(nuevo_autor)
        print("Lista de autores:")
        for autor in self.autores:
            print(autor)
    
    def listar_autores(self):
        return self.autores
    
harry1 = Libro([])
harry1.agregar_autor("Eduardo")
harry1.agregar_autor("JK")

print(harry1.listar_autores())