"""Crea una clase Conversor que permita convertir entre unidades (por ejemplo, kilómetros a millas).
"""

class Conversor: 

    @staticmethod
    def kilometros_a_millas(km):
        return km * 0.621371
    
    @staticmethod
    def millas_a_kilometros(millas):
        return millas / 0.621371
    
    @classmethod # si o si se debe poner la clase misma como primer argumento
    def millas_a_km(cls, millas):
        return millas / 0.621371
 
print(Conversor.kilometros_a_millas(5))
print(Conversor.millas_a_kilometros(3))
print(Conversor.millas_a_km(3))