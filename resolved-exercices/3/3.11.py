"""
Ejercicio 3.11 - Calificar estudiante
Para este ejercicio se debe implementar la función calificar_estudiante que tome la puntuación de un estudiante en un examen (un valor entre 0 y 100) como argumento y devuelva la calificación correspondiente en forma de letra según la siguiente escala:

Puntuación de 90 o más: “A” Puntuación de 80 a 89: “B” Puntuación de 70 a 79: “C” Puntuación de 60 a 69: “D” Puntuación por debajo de 60: “F”
"""

def calificar_estudiante(nota: int) -> str:
  if not (0 <= nota <= 100):
    return "Error"
  
  if nota >= 90:
    return "A"
  
  if nota >= 80:
    return "B"
  
  if nota >= 70:
    return "C"
  
  if nota >= 60:
    return "D"
  
  if nota < 60:
    return "F"
  
print(calificar_estudiante(95))  # Imprime: A
print(calificar_estudiante(82))  # Imprime: B
print(calificar_estudiante(70))  # Imprime: C
print(calificar_estudiante(65))  # Imprime: D
print(calificar_estudiante(45))  # Imprime: F