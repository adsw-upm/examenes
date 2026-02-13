---
id: ex-2017-01
year: 2017
exam: parcial 1 recuperacion
tags:
 - complejidad
---


Un ayuntamiento tiene una base de datos de 20.000 matrículas. Sobre estos datos el número de consultas es abrumadoramente superior al número de altas o bajas, por lo que solo nos preocuparemos por las consultas. Tenemos varias opciones para su implementación:
<ol>
<li> Un array ordenado, de 20.000 elementos; </li>
<li> Una tabla hash de con direccionamiento abierto (resolución interna de colisiones, sondeo por lista), de  20.000 posiciones; </li>
<li> Una tabla hash con listas de desbordamiento y 8.192 (2^13) posiciones; </li>
<li> Un árbol binario de búsqueda (BST). </li>
</ol>


- (a) (2,5 puntos) Para cada opción, indique los pros y los contras y elija razonadamente la estructura de datos que recomienda para el ayuntamiento. Debe argumentar en términos de espacio ocupado en memoria y del tiempo de búsqueda.

??? note "Mostrar solución"
    1. Pro: Ocupa la memoria imprescindible, sin nada extra; Tiempo $O(log n)$.

    2. Pro: Ocupa la memoria imprescindible y un poco más si se guardan los hashes; Contra: El tiempo de acceso se dispara al llegar al 100% de ocupación y es inviable.
    
    3. Contra: Ocupa memoria para los datos, para la tabla de acceso y para las listas de desbordamiento; Pro: El tiempo de acceso probable es $O(1)$, si los hashes se distribuyen uniformemente y las listas tienen una longitud acotada a unas pocas matrículas (menos de una docena); Contra: Aunque en el improbable caso peor sería $O(n)$.
    
    4. Contra: Ocupa memoria para los datos y para los enlaces entre nodos; Pro: Velocidad de acceso probable $O(log n)$; Contra: Aunque en el improbable caso peor sería $O(n)$.

    Óptimo:

    - por memoria ocupada: (1) Array ordenado;
    - por tiempo (probable) de acceso: (3) Tabla hash.
    
    Si la memoria no es un problema para 20.000 datos, la decisión se tomaría por tiempo de acceso: tabla hash (3).
    
    Si la memoria es la principal limitación, la mejor opción es el array ordenado (1).

