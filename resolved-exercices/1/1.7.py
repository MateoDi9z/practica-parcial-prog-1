"""
Ejercicio 1.7 - Modificaciones de los strings.
Modificar el string para que se le sume un año a la edad. Considerar que la edad va a tener siempre 2 caracteres.
"""

texto = "Felipe tiene 22 años"
edad = int(texto[13:15])
resultado = f"{texto[:12]} {edad + 1} {texto[16:]}!"
print(resultado)
