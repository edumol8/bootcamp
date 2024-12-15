from operaciones import suma as s, resta, multiplicacion, division

num1 =  int(input("Por favor ingrese el primer número: "))
num2 =  int(input("Por favor ingrese el segundo número: "))

print(f"la suma de {num1} + {num2} es: {s(num1, num2)}")
print(f"la resta de {num1} - {num2} es: {resta(num1, num2)}")
print(f"la multiplicacion de {num1} * {num2} es: {multiplicacion(num1, num2)}")
print(f"la division de {num1} // {num2} es: {division(num1, num2)}")
