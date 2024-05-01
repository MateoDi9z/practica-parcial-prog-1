"""
Ejercicio 3.7 - Información del rectángulo
Para este ejercicio se debe implementar la función informancion_del_rectangulo la cual debe imprimir en pantalla la 
información del área y el perímetro del rectaculo. Para lograr eso es necesario reutilizar las funciones creadas en los 
ejercicios anteriores
"""

def calcular_perimetro(base, altura):
    if base < 0 or altura < 0:
        return "El área del rectángulo no puede ser negativa"
    elif base == 0 or altura == 0:
        return 0
    return (base * 2) + (altura * 2)

def calcular_area(base, altura):
    if base < 0 or altura < 0:
        return "El área del rectángulo no puede ser negativa"
    return base * altura

def informancion_del_rectangulo(base, altura):
    print(f"Rectángulo con base {base} y altura {altura}:")
    print(f"Área: {calcular_area(base, altura)}")
    print(f"Perímetro: {calcular_perimetro(base, altura)}")

informancion_del_rectangulo(5,4)
# Imprime:
# Rectángulo con base 5 y altura 4:
# Área: 20
# Perímetro: 18