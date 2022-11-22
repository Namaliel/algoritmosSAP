# Algoritmo para calcular el factorial de cualquier número natural

## El factorial:

Primero  $0!=1$

Entonces para todo número mayor a $0$ se define al factorial como:
$\Pi_{k=1}^{n}k$

## El codigo:
~~~
00 Inicio
01 Leer variable "base"
02 Establecer el valor de la variable "reslutado" a 1
03 Estavlecer el valor de la variable "indice" a 1
04 verificar que el valor de la varialbe indice no sea igual al de la variable base
05 Si:
06  Establcer el valor de la variable resultado = resultado * base
07  Aumentar la variable indice en 1
08  Saltar al paso 04
09 No: 
10  Imprimir el valor de resultado
11  Saltar al paso 12
12 Fin
~~~
---
## Ejemplos de uso: 
### Python
```
$python3 factorial.py 3
> 6
```
### Julia
``` 
$julia factorila.jl 4
> 24
```

