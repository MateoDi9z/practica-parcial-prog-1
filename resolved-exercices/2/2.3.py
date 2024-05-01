"""
Ejercicio 2.3 - Costo de entradas del parque
Dados los siguientes costos para las entradas del parque de diversiones, se quiere saber cuanto deberá pagar un
adolescente con su abuelo.

Costos:
Niños hasta 4 años: $0 ( entrada gratis )
De 5 a 17 años: $50
De 18 a 50 años: $30
De 50 años en adelante: $10
"""

edad_adolescente = 14
edad_anciano = 66

cost = 0

if (5 <= edad_adolescente <= 17):
    cost += 50
if (18 <= edad_adolescente <= 50):
    cost += 30
if (18 <= edad_anciano <= 50):
    cost += 30
if (edad_anciano > 50):
    cost += 10
    
print(f"El costo de entrada para el grupo familiar es de: ${cost}")