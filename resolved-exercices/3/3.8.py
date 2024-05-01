"""
Ejercicio 3.8 - Invertir la oración
Para este ejercicio se debe implementar la función invertir_string la cuál recibe como parámetro un string y el cual se debe retornar de la función pero con todos sus caracteres de atrás hacía adelente.
"""

def invertir_string(txt: str) -> str:
  return txt[::-1]

print(invertir_string("Mateo"))