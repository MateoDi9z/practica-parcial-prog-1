"""
Ejercicio 1.2 - Uso del “slice” con un carácter
Obtener los siguientes datos del texto de ejemplo:

Primera letra ( usando índices positivos )
Última ( usando índices positivos )
Anteúltima letra ( usando índices negativos )
Primera letra ( usando índices negativos )
Es necesario que todos los caracteres se impriman en minúscula
"""

texto = "Hello, World!"

print(texto[0].lower())
print(texto[len(texto) - 1].lower())
print(texto[-2].lower())
print(texto[-len(texto)].lower())