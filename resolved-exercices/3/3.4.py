"""
Ejercicio 3.4 - Concatenar strings
Para este ejercicio se debe implementar la función concatenar_strings la cuál debe recibir como parámetros dos strings
( recomendamos llamarlos string_1 y string_2)
Y debe retornar la concatenación de ambos strings separados por un espacio
"""

def concatenar_strings(string_1: str, string_2: str) -> str:
    return string_1 + " " + string_2

print(concatenar_strings("Hola", "Mundo"))