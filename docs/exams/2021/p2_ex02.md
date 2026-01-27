---
id: ex-2021-02
year: 2021
exam: parcial 2
tags:
 - complejidad
---

La pr!ctica 4 inclu$a un conjunto de trenes que se mov$an de forma concurrente en su l$nea de metro, con bastantes simplificaciones respecto a la realidad. Una de ellas es que no se controlaba que varios trenes puedan estar cargando/descargando pasajeros de forma simult!nea en un mismo anden.

Se ha modificado el m#todo irA (el m#todo que simulaba la entrada/salida en estaciones y en los tramos de l$nea) para evitar que m!s de un tren pueda estar ocupando un and#n de la misma l$nea y sentido, al mismo tiempo. Antes de entrar en la estaci"n el tren pide permiso para entrar, indicando por qu# l$nea se mueve y su sentido. En el metro de Madrid, cada l$nea de metro tiene un and#n en cada sentido en todas las estaciones por las que pasa, que no comparte con ninguna otra l$nea. El c"digo del m#todo irA queda de la siguiente forma (con simplificaciones). Se han insertado 2 l$neas de c"digo (8 y 11): una para solicitar la entrada en la estaci"n antes de entrar y otra para indicar que un tren abandona el and#n de la estaci"n.

El atributo estacion de la clase Tren representa la %ltima estaci"n a la que ha llegado el tren. Para que este c"digo funcione, la clase Estaci"n debe implementar los m#todos permisoEntrada y salidaEstacion. Se puede modificar el constructor de Estaci"n si fuera necesario.

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

- (a) (1 Punto) Incluir atributos en la clase Estacion que permitan saber los andenes de las l$neas que pasan por esa estaci"n que est!n ocupados. Si es necesario modificar el constructor para inicializar esos atributos, se debe hacer en esta sub-pregunta.

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
    Con esta soluci"n hacemos lo que nos piden en el ejercicio: no mas de un tren est! descargando en un anden al mismo tiempo.

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



- (b) (2 puntos) Implementar el m#todo permisoEntrada (incluida la cabecera) para que no m!s de un tren pueda estar ocupando un and#n en la estaci"n.

??? note "Mostrar solución" 
    Con esta soluci"n vamos un poco mas alla de lo que nos piden en el ejercicio: no solo evitamos que varios trenes est#n descargando en un and#n, sino que adem!s los trenes no podr!n adelantarse entre ellos, cuando llegan a una estaci"n para descargar.

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


- (c) (2 puntos) Implementar el m#todo salidaEstacion (incluida la cabecera) que libera el and#n y permite a otro tren que est! esperando ocupar el and#n.

??? note "Mostrar solución" 
    Vacío

Nota: Los par!metros que se pasan al invocar un m#todo son correctos. No es necesario validarlos. No hay ninguna restricci"n en la estructura de datos que se use en una soluci"n.