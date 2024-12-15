#uso de lambda y map
from functools import reduce

numeros = [1, 2, 3, 4, 5] #lista
dobles = list(map(lambda x: x*2, numeros))
print(dobles)

#uso de filter
pares = list(filter(lambda x: x % 2 ==0, numeros))

impares = list(filter(lambda x: x % 2 ==1, numeros))

print(pares)
print(impares)


#uso de reduce
suma = reduce(lambda x, y: x +y, numeros)
print(suma)

