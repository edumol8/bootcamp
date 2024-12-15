# #Comprension de lista
# cuadrados = [x**2 for x in range(5)]
# print(cuadrados)

#generadores
# def contador():
#     for i in range(5):
#         yield i*2

# gen = contador()
# for valor in gen:
#     print(valor)


nombres = ["Maria", "Juan", "Pedro", "Luis"]
longitudes = {nombres: len() for nombre in nombres}
print(longitudes)