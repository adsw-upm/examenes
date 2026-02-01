---
id: ex-2025-06
year: 2025
exam: extraordinario
tags:
 - complejidad
---


- (a) (4 puntos) Modifique el código de sus prácticas para que las hebras resuelvan primero las tareas (TareaCamino) que tengan un camino más corto.

??? note "Mostrar solución"
    Modificaciones necesarias:
    **1. En la clase `TareaCamino`:**
    - Implementar la interfaz `Comparable<TareaCamino>`
    
    ```java
    class TareaCamino implements Comparable<TareaCamino> {
        public final Nodo nodoAVisitar;
        public final List<Nodo> caminoRecorrido;
    
        public TareaCamino(Nodo nodoAVisitar, List<Nodo> caminoRecorrido) {
            this.nodoAVisitar = nodoAVisitar;
            this.caminoRecorrido = caminoRecorrido;
        }
        
        @Override
        public int compareTo(TareaCamino otra) {
            return Integer.compare(this.caminoRecorrido.size(), 
                                  otra.caminoRecorrido.size());
        }
    }
    ```
    
    **2. En el método `getTarea()` de `PoolHebras`:**
    - Ordenar la lista antes de extraer la tarea
    
    ```java
    public synchronized TareaCamino getTarea(HebraWorker hw) throws InterruptedException {
        while (tareas.isEmpty() && hw.keepWorking) {
            wait();
        }
        if (!hw.keepWorking) {
            return null;
        }
        
        // Ordenar tareas por longitud de camino antes de extraer
        Collections.sort(tareas);
        return tareas.remove(0);
    }
    ```