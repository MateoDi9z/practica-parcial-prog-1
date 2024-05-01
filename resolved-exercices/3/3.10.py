"""
Ejercicio 3.10 - Es palindromo
Para este ejercicio se debe implementar la función es_palindromo que tome un string como argumento y retorne True si el string es un palíndromo y False si no lo es.
"""

def es_palindromo(txt: str) -> bool:
  return txt == txt[::-1]

print(es_palindromo("toyota"))
print(es_palindromo("racecar"))