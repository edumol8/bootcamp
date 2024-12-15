palabras = ["Python", "es", "genial", "y", "divertido"]
longitudes = [len(palabra) for palabra in palabras]
print(longitudes)


palabras = "python es divertido"
frecuencia = {letra: palabras.count(letra) for letra in set(palabras) if letra != ' '}
print(frecuencia)

def numeros_pares():
    for i in range(10):
        
        yield i * 2

gen = numeros_pares()
for numero in gen:
    print(numero)

