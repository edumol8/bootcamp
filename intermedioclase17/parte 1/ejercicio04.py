""""Crear una clase Vehículo con atributos marca y modelo. Crear una clase hija Coche con un atributo adicional velocidad_maxima.
"""

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima):
        super().__init__(marca, modelo)
        self.velocidad_maxima = velocidad_maxima

# class Moto(Vehiculo):
#     def __init__(self, marca, motor):
#         super().__init__(marca, None)
#         self.motor = motor


coche1 = Coche("ford", "mustang", 500 )
print(coche1.marca, coche1.modelo, coche1.velocidad_maxima)

# moto1 = Moto("susuki", "motor duro")
# print(moto1.marca, moto1.motor)
        