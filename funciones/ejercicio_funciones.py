numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)

doble = list(map(lambda x: x*2, numeros))
print(doble)

pares = list(filter(lambda x: x % 2 == 00, numeros))
print(pares)

from  functools import reduce
suma = reduce(lambda x, y: x+y, numeros )
print(suma)