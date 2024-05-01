"""
Ejercicio 3.3 - Dias a horas con reutilización
Implementar la función dias_a_horas_reutilizable, la cual tiene como parámetro un valor que puede ser entero o decimal
( recomandamos de llamarlo días) y va a retornar el valor de horas correspondiente. En caso de ser una cantidad de
horas negativa, se debe retornar un string con un mensaje de error

En este caso es requerido que dentro de la funcion dias_a_horas_reutilizable se haga uso de por lo menos una de las
funciones de este trabajo práctico para obtener el resultado.
"""

def dias_a_horas_reutilizable(dias):
    if dias < 0:
        return "Número erróneo de días ingresados"

    return f"{int(dias * 24)} horas"

horas_1 = dias_a_horas_reutilizable(5)
horas_2 = dias_a_horas_reutilizable(2.5)
horas_3 = dias_a_horas_reutilizable(0)
horas_4 = dias_a_horas_reutilizable(-4)

print(horas_1) # Imprime: 120 horas
print(horas_2) # Imprime: 60 horas
print(horas_3) # Imprime: 0 horas
print(horas_4) # Imprime: Número erróneo de días ingresados