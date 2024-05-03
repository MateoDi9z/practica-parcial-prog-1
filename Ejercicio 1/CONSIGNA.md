# Ejercicio 1 - Variables

Edita el archivo `main.py` para que al ejecutar el programa tome un pedido de un restaurante, siendo las entradas:

- Numero de orden: (Entero)
- Nombre de la persona: (String)
- Precio total: (Flotante)
- Estado del pago: (Booleano)

| **Tener en cuenta**

- Transforma los inputs a sus debidos tipos utilizando `int()`, `str()`, `float()` y `bool()` para que el código de error si un dato es incorrecto.
- Al mostrar el precio, recortar los decimales para que tenga solo 2 decimales de la siguiente forma, siendo la variable con el precio `precio`, para mostrar el dato con solo 2 decimales, usar `${precio:.2f}`
- Mostrar la parte **entera** del precio total (usando `int()`)

Luego imprimir en pantalla un resumen de la orden y calcular la propina siendo esta un 10% del total, en el siguiente formato:

`"Orden #<numero> - <nombre> - $<precio> (Propina: $<propina>) - Pago: <estado>"`

Para la siguiente entrada:

```sh
1. Numero de orden: 2
2. Nombre de la persona: Joe
3. Precio total: 100.9
4. Estado del pago: True
```

El programa debería responder con:

```sh
Orden #2 - Joe - $100 (Propina: $10.09) - Pago: True
```
