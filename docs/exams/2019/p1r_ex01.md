---
id: ex-2019-01
year: 2019
exam: parcial 1 recuperacion
tags:
 - complejidad
---

Se construye un árbol binario de búsqueda (BST) cuyos nodos contienen valores enteros.
- (a) (1,5 puntos) Dibuje la estructura del árbol resultante de insertar los valores 17, 11, 4, 21, 15, 18, en este orden.

??? note "Mostrar solución"
    ![](./p1r/p1r_ex01.png)


- (b) (1,5 puntos) Escriba el resultado que se obtiene al recorrer el árbol anterior en postorden.

??? note "Mostrar solución"
    4 15 11 18 21 17


- (c) (2 puntos) Se añade al árbol un número N de valores enteros, generados de forma aleatoria. Para N suficientemente grande, el tiempo necesario para ello depende de la complejidad de la operación de insertar valores en el árbol. Indique razonadamente cuál es esta complejidad, justificando el resultado.

??? note "Mostrar solución"
    Para insertar un valor hay que recorrer el árbol desde la raíz hasta encontrar el lugar apropiado donde meterlo. Si los valores se generan aleatoriamente podemos suponer que para N grande el árbol está equilibrado, y por tanto, el número de niveles que hay que recorrer es k, con N = 2k y k = log2 N. Por tanto, la complejidad del algoritmo es O (log N).