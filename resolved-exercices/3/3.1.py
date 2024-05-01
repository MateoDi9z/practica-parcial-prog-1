"""
Ejercicio 3.1 - Dias a horas
Implementar la función dias_a_horas, la cual tiene como parámetro un valor entero ( recomandamos de llamarlo días) y va
a retornar el valor de horas correspondiente. En caso de ser una cantidad de horas negativa, se debe retornar un string
con un mensaje de error
"""

def dias_a_horas(dias):
    if dias < 0:
        return "Número erróneo de días ingresados"

    return f"{dias * 24} horas"

horas_1 = dias_a_horas(5)
horas_2 = dias_a_horas(0)
horas_3 = dias_a_horas(-4)

print(horas_1) # Imprime: 120 horas
print(horas_2) # Imprime: 0 horas
print(horas_3) # Imprime: Número erróneo de días ingresados