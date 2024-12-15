#Eduardo Molina
try:
    num = int(input("Ingresa un numero: "))
except ValueError:
    print ("ERROR: Debe ingresar un numero")
else:
    print(f"El número {num} es válido")
finally:
    print("Gracias")


