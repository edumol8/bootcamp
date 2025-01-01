class Fraccion: 
    def __init__(self, numerador, denominador): 
        self.numerador = numerador 
        self.denominador = denominador

    def __eq__(self, otra):
        return self.numerador * otra.denominador == self.denominador * otra.numerador

    def __lt__(self, otra):
        return self.numerador * otra.denominador < self.denominador * otra.numerador

f1 = Fraccion(1, 2)
f2 = Fraccion(2, 4)
f3 = Fraccion(3, 4)

print(f1 == f2)  # True
print(f1 < f3)   # True
