"""Crea una clase Vector que permita sumar dos vectores usando el operador +.
"""

class Vector:
    def __init__(self, medida):
        self.medida = medida
    
    def sumar(self, otro_vector):
        return self.medida + otro_vector.medida

vector1 = Vector(5)
vector2 = Vector(10)

print(vector1.sumar(vector2))