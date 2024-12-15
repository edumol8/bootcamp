# try:
#     numero = int(input("Ingrese un numero: "))
# except ValueError as e:#poner que tipo de errror 
#     print(f"Error: {e}. Introduce un numero válido")
# else:
#     print(f"El numero es {numero}")
# finally:
#     print(f"fin del programa")

# numero = int(input("Ingrese un numero: "))

# print(f"El numero es {numero}")

class MiError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# try:
#     raise MiError("Mi mensaje de error")
# except MiError as e:
#     print(f"Error: {e}")

try:
    num = int(input("Introduce un número: "))
    resultado = 10/num
    print(f"El resultado es {resultado}")
except ValueError:
    print("Debes introducir un número")
except ZeroDivisionError:
    print("No se puede dividir entre cero")

