"""
Crear una funcion que que pida al usuario 2 notas y devuelva la mayor de ellas
"""

def devolver_notas(nota1, nota2):
    

    if nota1 > nota2:
        return nota1
    else:
        return nota2
    
nota1in= float(input("Ingresa la primera nota: "))
nota2in= float(input("Ingresa la segunda nota: "))

final = devolver_notas(nota1in, nota2in)
print("La mayor nota es:", final)