"""
Ejercicio 3.9 - Es par
Para este ejercicio se debe implementar la función es_par que tome un número como argumento y devuelva True si el número es par y False si no lo es.
"""

def es_par(n: int):
  return not n % 2

print(es_par(2))
print(es_par(1))