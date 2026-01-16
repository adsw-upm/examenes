---
id: ex-2017-01
year: 2017
exam: parcial 1 recuperacion
tags:
 - grafos
---

Dado el siguiente árbol binario:

![](./p1r/p1r_ex01.png)

- (a) (1,25 puntos) Escriba el resultado de recorrerlo en preorden.

??? note "Mostrar solución"
    J A M K Z

Un ayuntamiento tiene una base de datos de 20.000 matrículas. Sobre estos datos el número de consultas es abrumadoramente superior al número de altas o bajas, por lo que solo nos preocuparemos por las consultas. Tenemos varias opciones para su implementación:

    - 1) un array ordenado, de 20.000 elementos.
    - 2) una tabla hash de con direccionamiento abierto (resolución interna de colisiones, sondeo por lista), de  20.000 posiciones.
    - 3) una tabla hash con listas de desbordamiento y 8.192 (2^13) posiciones.
    - 4) un árbol binario de búsqueda (BST).

- (b) (2,5 puntos) Para cada opción, indique los pros y los contras y elija razonadamente la estructura de datos que recomienda para el ayuntamiento. Debe argumentar en términos de espacio ocupado en memoria y del tiempo de búsqueda.

??? note "Mostrar solución"
    1) + ocupa la memoria imprescindible, sin nada extra; * tiempo O(log n).

    2) * ocupa la memoria imprescindible y un poco más si se guardan los hashes; - el tiempo de acceso se dispara al llegar al 100% de ocupación y es inviable.
    
    3) - ocupa memoria para los datos, para la tabla de acceso y para las listas de desbordamiento; + el tiempo de acceso probable es O(1), si los hashes se distribuyen uniformemente y las listas tienen una longitud acotada a unas pocas matrículas (menos de una docena); - aunque en el improbable caso peor sería O(n).
    
    4) - ocupa memoria para los datos y para los enlaces entre nodos; + velocidad de acceso probable O(log n); - aunque en el improbable caso peor sería O(n).

    Óptimo:
    - por memoria ocupada: (a) array ordenado
    - por tiempo (probable) de acceso: (c) tabla hash
    
    Si la memoria no es un problema para 20.000 datos, la decisión se tomaría por tiempo de acceso: tabla hash (c).
    
    Si la memoria es la principal limitación, la mejor opción es el array ordenado (a)

Tenemos un árbol binario de búsqueda (BST) en el que cada nodo almacena un carácter. 

- (c) (1,25 puntos) Dibuje el árbolresultante de insertar en la secuencia indicada las letras: Q W E R T Y U I O P.

??? note "Mostrar solución"
    ![](./p1r/p1r_ex01sol.png)
