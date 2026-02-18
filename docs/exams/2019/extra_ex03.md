---
id: ex-2019-03
year: 2019
exam: extraordinario
tags:
 - hebras
---

Se quiere desarrollar un sistema de gestión de eventos. Este sistema está compuesto por un conjunto de productores y consumidores. Los productores ponen eventos en el sistema. Los consumidores recogen eventos del sistema para procesarlos.

- (a) Desarrolle el monitor `EventManager` con el siguiente esquema (Nota: el método `getEvents` tiene más peso en la calificación que el resto del código):
```java
public class EventManager {
    // Número máximo de eventos que se pueden almacenar
    public final int MAX_PENDING_EVENTS = ...;
    ...
    /**
    * Añadir un evento para procesar. Si el número de eventos pendientes de procesar
    * es igual al máximo, la hebra que llama se bloquea hasta que haya hueco
    */
    ... void putEvent (Event event) {...}
    /**
    * Recuperar eventos para su procesamiento. Este método admite que se soliciten
    * uno o dos eventos. El método deberá devolver un array con un número de eventos
    * igual a la solicitud. Las hebras que solicitan dos eventos tienen preferencia.
    * Si hay hebras bloqueadas y hay eventos suficientes, hay que desbloquear a las que
    * hayan solicitado dos eventos. Si no hay suficientes eventos pendientes para cada
    * tipo, se bloquea la hebra que llama hasta que haya suficientes.
    */
    ... Event[] getEvents (int nEventos) {...}
}
```

??? note "Mostrar solución"
    ```java
    public class EventManager {
        // Número máximo de eventos que se pueden almacenar
        public final int MAX_PENDING_EVENTS = 10;

        // Número de hebras que han solicitado dos eventos
        private int nTwoEvents = 0;

        // Lista de eventos añadidos y no recuperados
        private List<Event> buffer;

        public EventManager () {
            buffer = new ArrayList<>(MAX_PENDING_EVENTS);
        }

        /**
        * Añadir un evento para procesar. Si el número de eventos pendientes
        * de procesar es igual al máximo, la hebra que
        * llama se bloquea hasta que haya hueco
        */
        public synchronized void putEvent(Event event) {
            while (buffer.size() == MAX_PENDING_EVENTS) {
                try {
                    wait();
                } catch (InterruptedException ignored) {
                }
            }
            buffer.add(event);
            notifyAll();
        }
        /**
        * Recuperar eventos para su procesamiento. Este método admite que se soliciten
        * uno o dos eventos. El método deberá devolver un array con un número de eventos
        * igual a la solicitud. Las hebras que solicitan dos eventos tienen más urgencia.
        * Si hay hebras bloqueadas y hay eventos suficientes, hay que desbloquear a las que
        * hayan solicitado dos eventos. Si no hay suficientes eventos pendientes para cada
        * tipo, se bloquea a la hebra que llama hasta que haya suficientes.
        */
        Event[] getEvent(int nEvents) {
            Event[] events;

            if (nEvents == 2) nTwoEvents++;
            while ( (nEvents == 2 && buffer.size() < 2) ||
                    (nEvents == 1 && nTwoEvents > 0 && buffer.size() >= 2) ||
                    (buffer.size() == 0)) {
                try {
                    wait();
                } catch (InterruptedException ignored) {
                }
            }

            if (nEvents == 2) {
                nTwoEvents--;
                events = new Event[2];
                events[0] = buffer.remove(0);
                events[1] = buffer.remove(0);
            } else {
                events = new Event[1];
                events[0] = buffer.remove(0);
            }

            notifyAll(); return events;
        }
    }
    ```
