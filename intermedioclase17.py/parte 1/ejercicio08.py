"""Crear una clase Tienda que gestione un inventario. Implementar métodos para agregar, eliminar y mostrar productos."""

class Tienda:
    def __init__(self):
        self.inventario = {} #diccionario

    def agregar_producto(self, producto, cantidad):
        if producto in self.inventario:
            self.inventario[producto] += cantidad
        else:
            self.inventario[producto] = cantidad

    def eliminar_producto(self, producto):
        if producto in self.inventario:
            del self.inventario[producto]

    def mostrar_inventario(self):
        return self.inventario


tienda = Tienda()
tienda.agregar_producto("Manzanas", 10)
tienda.agregar_producto("Peras", 5)
tienda.eliminar_producto("Peras")
tienda.agregar_producto("Naranjas", 5)

print(tienda.mostrar_inventario())  # {'Manzanas': 10}