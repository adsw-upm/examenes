---
id: ex-2016-04
year: 2016
exam: extraordinario
tags:
 - monitores
---

En un sistema de comunicaciones hay un almacén con capacidad para N mensajes, con N comprendido entre MIN = 16 y MAX = 1024. Hay un cierto número de hebras (emisores) que almacenan mensajes en el almacén, y otras (receptores), que extraen mensajes de él. No se pueden almacenar mensajes si el almacén está lleno, ni se pueden extraer si está vacío.

El almacén se crea con capacidad MIN. Una hebra supervisora comprueba periódicamente su ocupación (número de mensajes almacenados), llamando al método adjust (ver esquema). Si la ocupación es mayor del 80 % de su capacidad, duplica la capacidad del almacén, siempre que sea posible sin sobrepasar el valor MAX. Si había emisores esperando por falta de espacio se les debe dar la oportunidad de enviar sus mensajes lo antes posible. Por otra parte, si la ocupación del almacén es menor que el 20 % de su capacidad, el supervisor reduce la capacidad a la mitad (pero nunca por debajo de MIN).

- (a) (5 puntos) Escriba una clase monitor que cumpla las condiciones anteriores, según el esquema que se da a continuación.

```java
public class Store {

    private static final int MIN = 5;

    private Message[] buffer;
    private int capacity;
    private int count = 0;
    private int in = 0;
    private int out = 0;

    // crea un almacén de capacidad MIN
    public Store() {
        this.capacity = MIN;
        this.buffer = new Message[capacity];
    }

    // almacena un mensaje en el almacén
    public synchronized void put(Message m) throws InterruptedException {
        while (count == capacity) {
            wait();
        }
        buffer[in] = m;
        in = (in + 1) % capacity;
        count++;
        notifyAll();
    }

    // extrae un mensaje del almacén
    public synchronized Message get() throws InterruptedException {
        while (count == 0) {
            wait();
        }
        Message m = buffer[out];
        buffer[out] = null;
        out = (out + 1) % capacity;
        count--;
        notifyAll();
        return m;
    }

    // ajusta la capacidad del almacén según la especificación
    public synchronized void adjust() {
        int newCapacity = Math.max(MIN, count);
        if (newCapacity == capacity)
            return;

        Message[] nuevo = new Message[newCapacity];
        for (int i = 0; i < count; i++) {
            nuevo[i] = buffer[(out + i) % capacity];
        }

        buffer = nuevo;
        capacity = newCapacity;
        out = 0;
        in = count;
        notifyAll();
    }
}
```

NOTA: Suponga que está definida la clase Message que se utiliza en este esquema.

??? note "Mostrar solución"
    ```java
    public class Store {

        private static final int MIN = 16;
        private static final int MAX = 1024;

        private int N;
        private List<Message> list = new ArrayList<>();

        // crea un almacén de capacidad inicial N
        public Store(int N) {
            this.N = Math.min(Math.max(N, MIN), MAX);
        }

        // almacena un mensaje en el almacén
        public synchronized void put(Message m) {
            while (list.size() >= N) {
                try {
                    wait();
                } catch (Exception ignored) {}
            }
            list.add(m);
            notifyAll();
        }

        // extrae un mensaje del almacén
        public synchronized Message get() {
            while (list.isEmpty()) {
                try {
                    wait();
                } catch (Exception ignored) {}
            }
            Message m = list.remove(0);
            notifyAll();
            return m;
        }

        // ajusta la capacidad del almacén según la especificación
        public synchronized void adjust() {
            if (list.size() > 0.8 * N) {
                N = Math.min(2 * N, MAX);
            }
            if (list.size() < 0.2 * N) {
                N = Math.max(N / 2, MIN);
            }
            notifyAll();
        }
    }
    ```
