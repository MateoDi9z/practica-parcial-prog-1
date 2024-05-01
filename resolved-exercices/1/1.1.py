"""
Ejercicio 1.1 - Uso del “not in”
Ingresar una oración usando input y verificar que no contenga ninguna letra con tilde Considerar que la letra puede ser mayuscula o minuscula.

Ayuda: los caracteres de las letras con tilde son distintos que los caracteres de las letras sin tildes ( por ejemplo, la letra á es un carácter distinto que la letra a)
"""

w = input(">").lower()

print(f"No contiene á: { 'á' not in w }")
print(f"No contiene é: { 'é' not in w }")
print(f"No contiene í: { 'í' not in w }")
print(f"No contiene ó: { 'ó' not in w }")
print(f"No contiene ú: { 'ú' not in w }")