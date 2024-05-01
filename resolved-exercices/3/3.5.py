"""
Ejercicio 3.5- Área rectángulo
Para este ejercicio se debe implementar la función calcular_area la cuál debe recibir como parámetros dos valores
numéricos que pueden ser int o float, el primero indicando la medida de la base del rectángulo y el segundo
representando la medida de la altura del rectángulo. Se debe retornar el cálculo del área del rectángulo que
representan.
"""

def calcular_area(base, altura):
    if base < 0 or altura < 0:
        return "El área del rectángulo no puede ser negativa"
    return base * altura

area_1 = calcular_area(5,4)
area_2 = calcular_area(3,-3)
area_3 = calcular_area(0,20)

print(area_1) # Imprime: 20
print(area_2) # Imprime: El área del rectángulo no puede ser negativa
print(area_3) # Imprime: 0