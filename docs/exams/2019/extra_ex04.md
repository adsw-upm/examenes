---
year: 2019
exam: extraordinario
tags:
 - hebras
---

A continuación se muestra el método `getEvent` de una versión alternativa de un gestor de eventos con prioridades, al que acceden concurrentemente varias hebras.
```java
public class Event {
    private EventInformation info;
    private EventPriority priority;
    // getters & setters
}
```

```java
public enum EventPriority {High, Low}
```

```java
import java.util.List;
import java.util.ArrayList;

public class PriorityEventManager {

    public final int MAX_PENDING_EVENTS = 10;
    private List<Event> list;

    public PriorityEventManager() {
        list = new ArrayList<>(MAX_PENDING_EVENTS);
    }

    public synchronized void putEvent(Event anEvent) {
        // implementación pendiente
    }

    public synchronized Event getEvent() {
        List<Event> aux = new ArrayList<Event>();
        Event event = null;

        // Copiar los elementos de list y guardarlos en aux
        aux.addAll(list);

        while (aux.size() == 0) {
            try {
                wait();
            } catch (InterruptedException e) {
            }
        }

        for (Event e : aux) {
            if (e.getPriority() == EventPriority.High) {
                event = e;
                aux.remove(e);
                break;
            }
        }

        if (event == null) {
            event = aux.remove(0);
        }

        list = aux;
        notifyAll();
        return event;
    }
}
```

- (a) (2,5 puntos) Razone si esta solución es correcta y, en caso contrario, describa los errores que contiene.

??? note "Mostrar solución"
    Esta solución es incorrecta en un programa concurrente. Cuando se ejecuta `GetEvent` se hace una copia de `list` a `aux`. Esta variable es local en cada instancia del método, por lo que sólo se puede cambiar al ejecutar la hebra que ha invocado este método. Eso quiere decir que si varias hebras han invocado a `GetEvent`, cada una tiene una variable `aux` local.

    Si la lista `aux` está vacía, por tanto, su tamaño es cero. En consecuencia, la hebra se quedará bloqueada en el `wait` y nunca volverá a ejecutarse, por que ninguna otra hebra podrá cambiar el valor de la variable `aux` local.

    Además, en el caso de que esta hebra se ejecutara, también hay varios errores en el código. Por ejemplo, cuando actualiza el valor de `list` machaca su versión actual.
    