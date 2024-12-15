#Eduardo Molina
texto = input("Ingresa un texto: ")

with open("ejercicio.txt", "w") as file:
    file.write(texto)

with open("ejercicio.txt", "r") as file:
    for linea in file:
        print(linea.strip())