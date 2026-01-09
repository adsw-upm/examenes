---
id: ex-2014-02
year: 2014
exam: extraordinario
tags:
 - monitores
---

Un sistema de gestión de un almacén de piezas está compuesto por un conjunto de productores y de consumidores, que se modelan mediante hebras. Las hebras productoras añaden piezas, mientras que las consumidoras las solicitan y retiran.

Se pide diseñar un monitor GestorPiezas que gestione las interacciones de estas hebras, cuya interfaz está formada por los siguientes métodos:
    … void solicitarPiezas (int cantidadPiezas): este método lo invocan las hebras consumidoras cuando quieren solicitar una cantidad de piezas determinada. Si hay piezas suficientes, se le proporcionan inmediatamente (se actualiza el número de piezas almacenadas). Si no las hay, se bloquea la hebra hasta que haya suficientes. En este caso, hay que bloquear al resto de hebras consumidoras hasta que se satisfaga la petición pendiente.
    
    … void agregarPiezas (int cantidadPiezas): este método lo invocan las hebras productoras para añadir piezas al almacén. La cantidad de piezas que se pueden almacenar es ilimitada.

Nota: el número de piezas debe ser positivo en todos los casos.

??? note "Mostrar solución"
    ```java
    public class GestorAlmacen {
        private int cantidadAlmacen = 0;
        private boolean peticionPendiente = false;
    
        public synchronized void solicitarPiezas(int cantidadPiezas)
            throws InterruptedException {
            while (peticionPendiente) wait();
            peticionPendiente = true;
            while (cantidadAlmacen < cantidadPiezas) wait();
            cantidadAlmacen = cantidadAlmacen - cantidadPiezas;
            peticionPendiente = false;
            notifyAll();
        }
    
        public synchronized void agregarPiezas(int cantidadPiezas)
            throws InterruptedException {
            cantidadAlmacen = cantidadAlmacen + cantidadPiezas;
            notifyAll();
        }
    }
    ```
