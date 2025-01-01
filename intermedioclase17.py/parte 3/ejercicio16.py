"""Crea una clase Contador que actúe como un iterador para contar hasta un número dado.
"""

class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.contador = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.contador < self.limite:
            self.contador += 1
            return self.contador
        else:
            raise StopIteration

contador = Contador(3)
for numero in contador:
    print(numero)  # 1 2 3