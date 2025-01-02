""""Crear una clase Persona con atributos nombre y edad., telefono direccion Implementar un método que devuelva si la persona es mayor de edad.
"""

class Persona:
    def __init__(self, nombre, edad, telefono, direccion):
        self.nombre = nombre
        self.edad= edad
        self.telefono = telefono
        self.direccion = direccion
    
    def mayor_de_edad(self):
        return self.edad >= 18


persona1 = Persona("Pablo", 36, "09909230923", "Portoviejo" )
print(persona1.mayor_de_edad())
print(persona1.telefono, persona1.direccion)
