"""
Ejercicio 3.6 - Perímetro rectángulo
Para este ejercicio se debe implementar la función calcular_perimetro la cuál debe recibir como parámetros dos valores
numéricos que pueden ser int o float, el primero indicando la medida de la base del rectángulo y el segundo
representando la medida de la altura del rectángulo. Se debe retornar el cálculo del perímetro del rectángulo que
representan.
"""

def calcular_perimetro(base, altura):
    if base < 0 or altura < 0:
        return "El área del rectángulo no puede ser negativa"
    elif base == 0 or altura == 0:
        return 0
    return (base * 2) + (altura * 2)

permietro_1 = calcular_perimetro(5,4)
permietro_2 = calcular_perimetro(3,-3)
permietro_3 = calcular_perimetro(0,20)

print(permietro_1) # Imprime: 18
print(permietro_2) # Imprime: El perímetro del rectángulo no puede ser negativo
print(permietro_3) # Imprime: 0