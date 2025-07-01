# Solicita al usuario que ingrese un número entero
numero = int(input("Introduce un número entero: "))

# Determina si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")