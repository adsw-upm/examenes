---
id: ex-2017-01
year: 2017
exam: extraordinario
tags:
 - complejidad
---

- (a) (?? puntos) ¿A qué orden de complejidad se debería aproximar la gráfica de tiempo de ejecución para los métodos de
ordenación por inserción y mezcla (merge sort ) ?

??? note "Mostrar solución"
    Inserción: O(n2); Mezcla: O(n·log n).


- (b) (?? puntos) La clase HashListas implementa tablas hash con listas de desbordamiento. En ella se define el método
```java
private int h(String s){...}
```
¿Para qué se usa este método?

??? note "Mostrar solución"
    Para calcular la posición del array que contiene la lista donde se almacena (o se podría almacenar) el elemento de clave s.


- (c) (?? puntos) En este ejercicio se usa un diccionario para almacenar palabras de un texto y el número de veces que aparecen. Una de las operaciones que se efectúan consiste en imprimir una lista con las n palabras más (o menos) usadas (método getTop()). En el ejercicio esto se implementa copiando los valores del diccionario a un array, que se ordena según el criterio elegido. Cuando se dice que esto se hace con “evaluación perezosa”, ¿qué significa esta expresión?

??? note "Mostrar solución"
    Que el array no se ordena hasta que es necesario, es decir hasta que se llama a getTop o a countBelow.

- (d) (?? puntos) En este ejercicio se usa una cola de paquetes que se puede implementar como un array o una lista. La cola está incluida en una clase, TsRouter, que tiene dos métodos públicos, send y get, que respectivamente añaden y recuperan paquetes de la cola. ¿Tienen que ser sincronizados estos métodos? ¿Por qué?

??? note "Mostrar solución"
    Sí, porque acceden a la cola, que es un objeto compartido por todas las hebras.

- (e) (?? puntos) En este ejercicio se utiliza sincronización de lectores y escritores para acceder a una estructura de datos compartida, la lista de manzanas del juego de la serpiente, encapsulada en la clase AppleListMonitor. ¿Qué cambios habría que hacer en esta clase para cambiar la sincronización de lectores y escritores por exclusión mutua?

??? note "Mostrar solución"
    Bastaría con suprimir las referencias a monitor.openReading / monitor.closeReading y a monitor.openWriting / monitor.closeWriting y hacer sincronizados todos los métodos de AppleListMonitor.

- (f) (?? puntos) En este ejercicio se utiliza un widget de tipo Button para lanzar el cálculo del índice de masa corporal. ¿Cómo se especifica qué método hay que ejecutar cuando se pulsa el botón?

??? note "Mostrar solución" 
    Se puede hacer de dos maneras: poniendo un atributo
    ```java
    Android:onClick=”método”
    ```
    en el layout correspondiente, o bien en Java, implementando la interfaz OnClickListener:
    ```java
    button.setOnClickListener(new OnClickListener() {
        @Override
        public void onClick(View v) {
            muestraMensaje(v);
        }
    });
    ```
    