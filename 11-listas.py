#Listas
lenguajes = ["pyhton", "c++","go", "java", "javascript"]
# print(type)

print(lenguajes) #toda la lista
print(lenguajes[1]) #elemento específico
#lenguajes[1]="ruby"
print(lenguajes)

print(lenguajes[1:4])#no imprime el ultimo, llega hasta el  

print(lenguajes[:3])
print(lenguajes[-1])
print(lenguajes[2:])

lenguajes.insert(3, "Dart")
print(lenguajes)

#borras
lenguajes.remove("Dart")
print(lenguajes)

#busqueda
print("php" in lenguajes)
print("go" in lenguajes)

#longitud
print(len(lenguajes))





