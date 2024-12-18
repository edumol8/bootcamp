lenguajes = {"pyhton", "c++", "go", "java", "java", "javascript" }

print(type(lenguajes))
lenguajes.add("php")
print(lenguajes)

# print(lenguajes.clear())
# print(lenguajes)
lenguajes2 = lenguajes.copy()
print(lenguajes2)

lenguajes2.pop() #elimina el dato inicial
print(lenguajes2)
print(lenguajes)

print(lenguajes2.intersection(lenguajes))