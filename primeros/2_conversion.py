"""
este script coniverte una temp ingresada por el usuario de farenheit a celcius o de celsius a farneheit, dependiendo de la escala proporcionada
"""

escala = (input("Ingresa F si es Farenheit o C si es Celsius: "))
temp = float(input("cual es la temperatura?"))

conversion = 0

if escala == "C" or escala == "c":
   conversion = ((temp * 1.8) + 32)
   print("la temp es ", conversion)

elif escala == "F" or "f":
   conversion = (temp-32)/1.8
   print("la temp es ", conversion)
else:
   print("escala no válida")