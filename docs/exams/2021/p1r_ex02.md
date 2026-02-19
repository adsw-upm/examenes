---
id: ex-2021-02
year: 2021
exam: parcial 1 recuperacion
tags:
 - grafos
---

Se quiere desarrollar un sistema para calcular de forma eficiente las notas medias en la UPM a diferentes niveles. Nos interesan las notas medias a nivel de asignatura, a nivel de Escuela, y a nivel de Universidad. Se quiere que cada vez que se publique la nota de una asignatura se recalculen las medias a nivel de Escuela y Universidad, sin realizar operaciones innecesarias.

Para ello, utilizaremos una estructura de árbol de 3 niveles:

- El nodo raíz es la universidad (UPM).
- El nodo raíz (UPM) tiene un hijo por cada escuela (p.e., ETSIT, ETSAM).
- Cada escuela tiene un hijo por cada asignatura que se imparte en esa escuela (p.e., ADSW, CORE).
- Cada nodo tiene una referencia a todos sus hijos (`this.hijos`), y a su nodo padre (`this.padre`, que será `null` para el nodo raíz).

Inicialmente se propone una estrategia de carga ansiosa (*eager loading*), en la que cada vez que se actualiza una nota de una asignatura se actualizan las medias de todos los nodos necesarios.

Se considera que actualizar un nodo es necesario cuando alguno de sus descendientes ha sido modificado desde el último cálculo.

Cada `Nodo` tiene los siguientes atributos:

![](./p1r/p1r_ex01.png)

Sea `E` el número de escuelas, y `A` el número de asignaturas, suponiendo que la distribuci%n de asignaturas por escuela es uniforme, se pide:

- (a) (2,5 puntos) Implementar los algoritmos para modificar y recuperar la nota media de un nodo para la estrategia de carga ansiosa, utilizando las siguientes firmas:
```java
void setNota(float nota, int peso) { // a rellenar por el alumno }
float getNota() { // a rellenar por el alumno }
```

??? note "Mostra solución"
    ```java
    public float getNota() {
        return this.nota;
    }

    /* 
     * Actualiza la nota de este nodo y recalcula los antecesores.
     */
    public void setNota(float nota, int peso) {
        // Se podría añadir lógica para solo modificar la nota
        // de las Asignaturas, no del resto de nodos.
        this.peso = peso;
        this.nota = nota;

        if (this.padre != null) {
            recalcular(this.padre);
        }
    }

    public static void recalcular(Nodo raiz) {
        float media = 0;
        int peso = 0;

        for (Nodo hijo : raiz.hijos) {
            media += hijo.peso * hijo.nota;
            peso += hijo.peso;
        }

        media = media / peso;
        raiz.nota = media;
        raiz.peso = peso;
        raiz.actualizado = true;

        if (raiz.padre != null) {
            recalcular(raiz.padre);
        }
    }
    ```

    En el enunciado no se especifica el rol del peso, así que se dan por válidas las soluciones que asumen el mismo peso para todos los nodos.


- (b) (0,5 puntos) Los algoritmos implementados, ¿Son recursivos o iterativos?.

??? note "Mostra solución"
    La implementación de `setNota` se basa en el método calcular, que es recursivo. Se podría implementar de manera iterativa.


- (c) (0,5 puntos) Estimar la complejidad de modificar la nota de 1 sola asignatura, y de modificar todas las asignaturas, en función de `A` y `E`.

??? note "Mostra solución"
    Al actualizar una asignatura, se debe recalcular la nota de la escuela, y luego de la universidad. Habrá `A/E` asignaturas por escuela (distribución uniforme). Por tanto:

    $O(setNota() = O(A/E + E)$

    $O(setNotaTodas) = O(A * (A/E + E))$

    Por completitud, la complejidad de consultar una nota es constante (ya se calcula en el `setNota).


Para mejorar el rendimiento, se propone comparar la estrategia anterior con otra de carga perezosa (*lazy loading*), en la que sólo se actualizan las notas necesarias al acceder a una nota desactualizada.

- (d) (0,5 puntos) Estime la complejidad de modificar 1 sola asignatura, y de modificar todas las asignaturas, para el caso de carga perezosa, en función de `A` y `E`.

??? note "Mostra solución"
    Con carga perezosa, cuando se modifica una nota se marcan los nodos superiores al nodo a actualizar como desactualizados. Esa operación para cada asignatura depende sólo del número de niveles (en este caso, 3). Por tanto:
    
    $O(setNota() = O(1)$
    
    $O(setNotaTodas) = O(A)$, es decir, $A * O(setNota1)$
    
    Aunque no se especifica en el enunciado, la complejidad de `getNota(UPM)` para esta estrategia tras haber modificado 1 o TODAS las notas, sería:

    $O(getNota1(UPM)) = O((A/E) + E)$, sólo recalcula una de las ramas del árbol.

    $O(getNotatodas) = O(A + E)$, recalcula todos los nodos


- (e) (1 punto) En lugar de tener 3 niveles (universidad, escuela, asignatura), se modifica el árbol para que sea un árbol binario perfectamente balanceado (cada nodo padre tiene exactamente 2 hijos). Calcule la complejidad de acceder a la nota UPM para el caso de carga perezosa tras cambiar una sola asignatura, en función de `A`.

??? note "Mostra solución"
    Como hemos visto en el anterior apartado, la diferencia es que en un caso recalcula una rama, y en el otro recalcula el árbol entero.
    
    En este caso, tendremos que calcular el n&mero de niveles. Al tratarse de un árbol binario, con un número de hojas `A`, el número de niveles será $log2(A)$.
    
    El número total de nodos será la suma de nodos en cada uno de los niveles:
    
    $N = A + A/2 + A/4 + ' 1 ~= 2*A$
    
    $O(getNota1(UPM)) = O(log(A))$, en cada nodo se suman los dos nodos inferiores.

    $O(getNotaTodas) = O(N) = O(A)$.