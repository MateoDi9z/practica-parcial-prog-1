"""
Ejercicio 2.4 - Comparación de strings
Dados los siguientes días de la semanana, verificar que sean dias laborables o de fin de semana
Se debe usar por lo menos un or o and para resolverlo
"""

dia_1 = "Martes"
dia_2 = "Domingo"
dia_3 = "Octodia"

def dia_laborable(dia):
    dia = dia.lower()
    if (dia == "sabado") or (dia == "domingo"):
        print(f"El día {dia.title()} es un día de fin de semana")
    elif dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves" or (dia == "viernes"):
        print(f"El día {dia.title()} es un día laborable")
    else:
        print(f"El día {dia.title()} no es válido")

dia_laborable(dia_1)
dia_laborable(dia_2)
dia_laborable(dia_3)