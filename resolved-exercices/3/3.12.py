"""
Ejercicio 3.12 - Verificar positividad
Para este ejercicio se debe implementar la función verificar_positividad que recibe como parámetro un número y retorna información sobre si este número es positivo, negativo o cero.
"""

def verificar_positividad(n) -> str:
  if n == 0:
    return "El número es cero."
  if n > 0:
    return f"El número {n} es positivo."
  return f"El número {n} es negativo"

print(verificar_positividad(5))   # Imprime: El número 5 es positivo.
print(verificar_positividad(-3))  # Imprime: El número -3 es negativo.
print(verificar_positividad(0))   # Imprime: El número es cero.