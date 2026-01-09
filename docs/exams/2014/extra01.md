---
id: ex-2014-01
year: 2014
exam: extraordinario
tags:
 - complejidad
---

- (a) (2,5 puntos) En una matriz de valores enteros de dos dimensiones, se dice que un elemento es un pico si es mayor o igual que sus cuatro vecinos en vertical y horizontal (o sus tres vecinos, en el caso de que se encuentre en el borde de la matriz, o sus dos vecinos si está en una esquina).

Para encontrar un pico en una matriz de N filas por M columnas (se puede demostrar que siempre existe al menos uno) se puede utilizar el siguiente algoritmo:
    1. Si M es igual a 1, encontrar el mayor valor de esa columna, y devolverlo como resultado.
    2. En otro caso, encontrar el mayor valor en la columna central de la matriz.
    3. Si ese valor es mayor o igual que sus vecinos derecho e izquierdo (si existen), devolverlo como resultado.
    4. En otro caso, si ese valor es menor que su vecino izquierdo (si existe), continuar el mismo algoritmo con la mitad izquierda de la matriz. Y si no es así, continuar el mismo algoritmo con la mitad derecha de la matriz (quitando la columna central en ambos casos).

Se pide indicar razonadamente cuál es la complejidad del algoritmo descrito, en términos de N y M.

??? note "Mostrar solución"
    La búsqueda del mayor valor en una columna de N enteros tiene complejidad N, ya que todos los valores de la columna han de ser comprobados, y las operaciones a realizar con cada uno de ellos son de complejidad constante. 

    Por otra parte, en el peor caso habrá que hacer esa búsqueda tantas veces como se puedan dividir iterativamente en dos partes iguales las M columnas, para llegar al final a una sola. Es decir, logaritmo en base dos de M veces. Por tanto, la complejidad total del algoritmo es N*log(M).