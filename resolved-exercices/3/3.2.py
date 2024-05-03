"""
Ejercicio 3.2 - Dias a horas con fracciones
Implementar la función dias_a_horas_con_fracciones, la cual tiene como parámetro un valor decimal ( es decir, float,
recomandamos de llamarlo días al igual que en dias_a_horas) y va a retornar el valor de horas correspondiente. En caso
de ser una cantidad de horas negativa, se debe retornar un string con un mensaje de error
"""

def dias_a_horas_con_fracciones(dias):
    if dias < 0:
        return "Número erróneo de días ingresados"

    return f"{int(dias * 24)} horas"

horas_1 = dias_a_horas_con_fracciones(5)
horas_2 = dias_a_horas_con_fracciones(2.5)
horas_3 = dias_a_horas_con_fracciones(0)
horas_4 = dias_a_horas_con_fracciones(-4)

print(horas_1) # Imprime: 120 horas
print(horas_2) # Imprime: 60 horas
print(horas_3) # Imprime: 0 horas
print(horas_4) # Imprime: Número erróneo de días ingresados
