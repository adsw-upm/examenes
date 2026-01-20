---
id: ex-2017-01
year: 2017
exam: extraordinario
tags:
 - complejidad
---

A pesar de que un genoma tiene más de dos gigas de (solo cuatro tipos distintos de) bases (A, G, C, T), la mayor parte del mismo es “basura”, pues solo una pequeña fracción de subsecuencias (contiguas) del mismo codifica la producción de aminoácidos, es decir, proteínas. A esas subsecuencias significativas de bases se les conoce con el nombre de genes.

Las subsecuencias que constituyen genes son de longitud moderada, entre cien y mil bases, y tienen la característica de que al menos una de las cuatro bases se presenta en dicha subsecuencia con (mucha) menor frecuencia que las otras tres. Digamos, por ejemplo, 20 por ciento menos. Interpretado este porcentaje sobre el número total de bases de la subsecuencia considerada.

- (a) (5 puntos) Se pide diseñar un algoritmo (no un programa) que, a partir de un genoma especificado como una (muy) larga secuencia de bases, encuentre los genes de longitud 300 bases. Y a continuación, analizar la complejidad en espacio y en tiempo de dicho algoritmo en términos del tamaño del genoma.

??? note "Mostrar solución"
    Se supone declarada una clase, llamémosla Contadores, con cuatro atributos enteros de valor inicial cero, que se van a usar para contar del número de cada tipo de base que hay, desde el principio del genoma hasta un punto dado. Y se supone también que tenemos un array, llamémosle ultimas300, que mantiene el valor de los cuatro contadores para cada uno de los últimos 300 puntos del genoma que hemos visitado, según lo exploramos desde el principio hasta el final de su cadena de bases.
    
    El algoritmo es:
        1) Ir leyendo de un fichero el genoma base a base desde el principio hasta su posición 299, actualizando los contadores de ultimas300 en las posiciones 0-298.
        2) Leer la siguiente base del genoma, incrementar el contador correspondiente a esa base en la última posición actualizada del array en una unidad, y guardar los cuatro valores actuales en la siguiente posición de ultimas300, manejando este array de manera circular (la posición siguiente a la 299 es la cero).
        3) Restar de los cuatro contadores actuales los contadores que están en el array 299 posiciones antes (de manera circular también). Si uno de esos cuatro valores es menor que 60 (=300/4*0.8), hemos encontrado un gen y lo imprimimos.
        4) Si aún quedan bases por leer en el genoma, volvemos al punto 2). En otro caso, hemos acabado el algoritmo.
    
    La complejidad en espacio es constante, pues el tamaño de ultimas300 es fijo, no depende del tamaño del genoma. En cuanto a la complejidad en tiempo, la parte 1) es también constante, ya que tampoco depende del tamaño del genoma. Mientras que las partes 2), 3) y 4) se ejecutan una vez por cada base del genoma (exceptuando las 299 primeras, valor constante). Y como resulta que esas tres partes tienen una complejidad constante, se tiene:
    
    C1 + C2*O(n-299) + C3*O(n-299) + C4*O(n-299) = (C1 - 299*(C2+C3+C4)) + (C2+C3+C4)*O(n) = C5 + C6*O(n) = C6*O(n) = O(n)
    
    Es decir, el algoritmo tiene una complejidad lineal en el tiempo.