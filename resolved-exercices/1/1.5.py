"""
Ejercicio 1.5 - Uso del “slice” validando que la palabra obtenida está contenida en otro string
Se debe obtener del texto dado sus primeros 2 caracteres y concatenarlos con lo últimos 3. Con este string obtenido
se debe validar que el mismo se encuentre o no dentro de la lista de gases nobles.

Considerar que las palabras pueden tener algunos caracteres en mayúscula. Al momento de realizar la validación se debe
utilizar todo en minúscula
"""

gases_nobles = "Helio, Neón, Argón, Kriptón, Xenón, Radón, Oganesón"
texto = "Hello, Aurelio"

new_texto = (texto[0:2] + texto[-3:]).lower()
print(f"La palabra se encuentra dentro de los gases nobles: {new_texto in gases_nobles}")