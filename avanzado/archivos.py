# #Escritura de archivo

# #w es escribir
# with open('archivo.txt', 'w') as f: 
#     f.write("Hola mundo developers!\n")

# #r es read
# with open('archivo.txt', 'r') as f:
#     contenido= f.read() #terminar siempre con ()
#     print(contenido)


#Imagenes
# with open('logo.png', 'r') as file:
#     datos = file.read() 

with open("saludo.txt", "w") as file:
    file.write("Hola, mundo")

with open("saludo.txt", "r") as file:
    for linea in file:
        print(linea.strip())