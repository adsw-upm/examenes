---
id: ex-2021-02
year: 2021
exam: parcial 2
tags:
 - complejidad
---

La práctica 4 incluía un conjunto de trenes que se movían de forma concurrente en su línea de metro, con bastantes simplificaciones respecto a la realidad. Una de ellas es que no se controlaba que varios trenes puedan estar cargando/descargando pasajeros de forma simultánea en un mismo anden.

Se ha modificado el método `irA` (el metodo que simulaba la entrada/salida en estaciones y en los tramos de línea) para evitar que m!s de un tren pueda estar ocupando un andén de la misma línea y sentido, al mismo tiempo. Antes de entrar en la estación el tren pide permiso para entrar, indicando por qué línea se mueve y su sentido. En el metro de Madrid, cada línea de metro tiene un andén en cada sentido en todas las estaciones por las que pasa, que no comparte con ninguna otra línea. El código del método `irA` queda de la siguiente forma (con simplificaciones). Se han insertado 2 líneas de código (8 y 11): una para solicitar la entrada en la estación antes de entrar y otra para indicar que un tren abandona el andén de la estación.

El atributo `estacion` de la clase `Tren` representa la última estación a la que ha llegado el tren. Para que este código funcione, la clase Estación debe implementar los métodos `permisoEntrada` y `salidaEstacion`. Se puede modificar el constructor de `Estación` si fuera necesario.

```java
01  TrayectoLineaMetro tr=linea.getSecuenciaMovimientos(origen,destino,ida);
02  pasos.add(estacion);
03  while (!tr.finMovimiento()) {
04     Tramo c=tr.siguienteMovimiento();
05     linea.getMapa().mueve(this, c);
06     pasos.add(c.hasta());
07     estacion=c.hasta();
08     estacion.permisoEntrada(linea,ida);
09     linea.getMapa().entraEnEstacion(this, c);
10     linea.getMapa().desembarca(this, c.hasta());
11     estacion.salidaEstacion(linea,ida);
12  }
13     if (!pasos.contains(destino))
14     pasos.add(destino);
```

Asumiendo que los parámetros que se pasan al invocar un método son correctos, es decir, no es necesario validarlos, y no hay ninguna restricción en la estructura de datos que se use en una solución. Se pide:

- (a) (1 Punto) Incluir atributos en la clase `Estacion` que permitan saber los andenes de las líneas que pasan por esa estación que están ocupados. Si es necesario modificar el constructor para inicializar esos atributos, se debe hacer en esta sub-pregunta.

```java
// Constructor: id: identificador de estación, posición de la estación en el mapa,
// tiempo de espera en los andenes, nombre de la estación
public Estacion(int id, Vector posicion, double tiempo, String nombre) { ... }

// Indica cuando un tren que circula por la Linea l y sentido ida o vuelta, quiere entrar en la estación
... void permisoEntrada(LineaMetro l, boolean ida) { ... }

// Indica cuando un tren que circula por la Linea l y sentido ida o vuelta, abandona la estación
... void salidaEstacion(LineaMetro l, boolean ida) { ... }
```

??? note "Mostrar solución" 
    Con esta solución hacemos lo que nos piden en el ejercicio: no mas de un tren está descargando en un anden al mismo tiempo.

    ```java
    private Set<LineaMetro>[] andenes = new Set[2];
    
    public EstacionS(int id, Vector posicion, double tiempo, String nombre) {
        andenes[0] = new HashSet<LineaMetro>();
        andenes[1] = new HashSet<LineaMetro>();
    }
    
    // Indica cuando un tren que circula por la Linea l y sentido ida o vuelta,
    // quiere entrar en la estación
    public synchronized void permisoEntrada(LineaMetro l, boolean ida) {
        while (andenes[ida ? 1 : 0].contains(l)) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        andenes[ida ? 1 : 0].add(l);
    }
    
    // Indica cuando un tren que circula por la Linea l y sentido ida o vuelta,
    // abandona la estación
    public synchronized void salidaEstacion(LineaMetro l, boolean ida) {
        if (!andenes[ida ? 1 : 0].contains(l)) {
            throw new RuntimeException(
                "No podemos salir de un anden si no estamos dentro"
            );
        }
        andenes[ida ? 1 : 0].remove(l);
        notifyAll();
    }
    ```



- (b) (2 puntos) Implementar el método `permisoEntrada` (incluida la cabecera) para que no más de un tren pueda estar ocupando un andén en la estación.

??? note "Mostrar solución" 
    Con esta solución vamos un poco mas alla de lo que nos piden en el ejercicio: no solo evitamos que varios trenes están descargando en un andén, sino que adem!s los trenes no podrán adelantarse entre ellos, cuando llegan a una estación para descargar.

    ```java
    private Map<LineaMetro, List<Thread>>[] andenes = new Map[2];

    public Estacion(int id, Vector posicion, double tiempo, String nombre) {
        andenes[0] = new HashMap<LineaMetro, List<Thread>>();
        andenes[1] = new HashMap<LineaMetro, List<Thread>>();
    }

    // Indica cuando un tren que circula por la Linea l y sentido ida o vuelta,
    // quiere entrar en la estación
    public synchronized void permisoEntrada(LineaMetro l, boolean ida) {
        if (andenes[ida ? 1 : 0].get(l) == null) {
            andenes[ida ? 1 : 0].put(l, new ArrayList<Thread>());
        }

        andenes[ida ? 1 : 0].get(l).add(Thread.currentThread());

        while (andenes[ida ? 1 : 0].get(l).get(0) != Thread.currentThread()) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    // Indica cuando un tren que circula por la Linea l y sentido ida o vuelta,
    // abandona la estación
    public synchronized void salidaEstacion(LineaMetro l, boolean ida) {
        if (andenes[ida ? 1 : 0].get(l).get(0) != Thread.currentThread()) {
            throw new RuntimeException(
                "El tren que no esta en el anden no puede salir de la estacion"
            );
        }

        andenes[ida ? 1 : 0].get(l).remove(Thread.currentThread());
        notifyAll();
    }
    ```


- (c) (2 puntos) Implementar el método `salidaEstacion` (incluida la cabecera) que libera el andén y permite a otro tren que está esperando ocupar el andén.

??? note "Mostrar solución" 
    Vacío
