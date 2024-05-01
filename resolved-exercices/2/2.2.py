"""
Ejercicio 2.2 - Comparación de números
Teniendo las 3 siguientes variables con valores numéricos se quiere realizar las comparaciones entre las mismas y saber cuál es el mayor y cual es el menor de los 3 números.
"""

a = 4
b = -5
c = 2

# Opción 1
print(f"El número mayor es: {max(a, b, c)}")
print(f"El número menor es: {min(a, b, c)}")

# Opción 2
# if (a > b and a > c):
#     print(f"El número mayor es: {a}")
# elif b > a and b > c:
#     print(f"El número mayor es: {b}")
# else:
#     print(f"El número mayor es: {c}")
#
# if (a < b and a < c):
#     print(f"El número menor es: {a}")
# elif b < a and b < c:
#     print(f"El número menor es: {b}")
# else:
#     print(f"El número menor es: {c}")