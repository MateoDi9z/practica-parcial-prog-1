# Ejercicio 2 - Strings

Edita el archivo `main.py` para que al ejecutar el programa devuelva los siguientes datos, haciendo uso de la variable `base_de_datos`, la cual es un String con nombres de alumnos.

Definir las variables `nombre1`, `nombre2` y `nombre3` y que cada este una este definida con un nombre de la base de datos (Para la variable `nombre1` usar el primer nombre y asi sucesivamente).

a. El primer nombre tiene que estar invertido, es decir, la primer palabra tiene que ser la ultima y asi sucesivamente

b. El segundo nombre tiene que ser modificado para que este sea igual a, la suma entre dos slices, siendo una desde el tercer caracter hasta el cuarto y la otra, las ultimas dos del letras del nombre

c. El ultimo nombre, tiene que estar invertido y a su vez tiene que saltearse una letra por cada letra, por ejemplo, para "holamundo" seria "onmlh"

Por ultimo, la funcion main tiene que _retornar_ los tres nombres modificados concatenados en orden alfabetico. (Opcional)

Ejemplo para 3 nombres

```sh
nombre1 = "agustin"
nombre2 = "matias"
nombre3 = "bautista"
```

El resultado sera:

```sh
nombre1 => nitsuga
nombre2 => tias
nombre3 => asta
```

Y la funcion `main()` retornara: `astanitsugatias`
