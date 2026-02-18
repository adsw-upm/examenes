---
id: ex-2019-01
year: 2019
exam: extraordinario
tags:
 - ???
---

Una empresa de telecomunicaciones necesita gestionar una tabla de abonados con sus números de línea correspondientes. Para ello utiliza una clase Java denominada `TablaAbonados` con la interfaz que se especifica a continuación:
```java
public class TablaAbonados {
    ...
    /**
    * Registrar una nueva línea
    * @param numero línea
    * @param abonado apellidos, nombre
    */
    public void insertar (String numero, String abonado) {...}
    /**
    * Eliminar el registro de una línea
    * @param numero de línea
    */
    public void eliminar (String numero) {...}
    /**
    * Apellidos y nombre del titular de una línea
    * @param numero de línea
    * @return apellidos, nombre
    */
    public String abonado (String numero) {...}
}
```

Las operaciones insertar y abonado se ejecutan muchas veces al día, y la operación eliminar se ejecuta con menos frecuencia. Para implementar la tabla se utiliza internamente una tabla hash con listas.

Nota: no escriba código, sólo indique qué algoritmos habría que utilizar

- (a) (1 punto) Explique razonadamente qué parámetros se deben tomar como clave y valor, respectivamente, en la tabla hash.

??? note "Mostrar solución"
    Un número de línea permite identificarla de forma unívoca, mientras que los abonados se pueden repetir, por ejemplo, si un abonado tiene varios números. Por tanto, se debe usar el número como clave y el abonado como valor en la tabla.


- (b) (1 punto) Si el número máximo de abonados de empresa se puede estimar en 1.000.000, aproximadamente, indique razonadamente cuál sería el número mínimo de ranuras (*slots*) de la tabla hash para obtener un comportamiento eficiente.

??? note "Mostrar solución"
    Para mantener la complejidad $O(1)$ en las operaciones con la tabla hash, el número $k$ de ranuras debe ser significativamente superior al número de claves, $N$. Por ejemplo, si se quiere mantener la carga de la tabla por debajo del 50% harían falta 2.000.000 de ranuras


- (c) (1,5 puntos) Indique cuál sería la complejidad que se puede esperar de las operaciones de la tabla para el caso anterior, justificando la respuesta.

??? note "Mostrar solución"
    Para una tabla hash con listas y una carga reducida, el tiempo de acceso para las operaciones de la tabla sería $t=th+top≈constante$. Por tanto, para $N$ grande se puede suponer $t\in O(1)$.


- (d)  (1,5 puntos) Una vez al trimestre la empresa debe entregar a la administración, a efectos fiscales, una lista de abonados ordenada alfabéticamente. Para ello se añade a la clase anterior un nuevo método:
```java
public List<String> listaAbonados (String) {...}
```

que genera la lista a partir del contenido de la tabla hash. Explique, justificando la respuesta, cómo se podría generar esta y cuál sería la complejidad de la operación `listaAbonados` (1,5 puntos).

??? note "Mostrar solución"
    Para obtener la lista ordenada hay que efectuar las siguientes operaciones:

    - Obtener una lista con todos los elementos de la tabla hash: Para ello hay que recorrer toda la tabla, y por tanto esta operación tiene complejidad lineal, $O(N)$;
    - Ordenar la lista: Si se usa un algoritmo de ordenación eficiente, como `QuickSort` o `MergeSort`, la complejidad de esta operación es, en promedio, $O(Nlog N)$.

    Por tanto, la complejidad total de la operación será $O(N)+O(NlogN)≈O(NlogN)$.
