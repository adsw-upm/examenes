---
id: ex-2016-03
year: 2016
exam: extraordinario
tags:
 - hebras
---

En un programa de supervisión y control de una central térmica, existen un conjunto de hebras que toman la temperatura del vapor en distintos puntos de la caldera regularmente y la almacenan junto con la hora de la medida, para que posteriormente otro conjunto de hebras pueda leer la última temperatura y hora medidas y realizar cálculos con ellas. Y se desea que cada una de las hebras del primer conjunto almacene la temperatura y hora medidas con exclusión mutua de todas las demás hebras, pero que cualquier número de hebras del segundo tipo pueda estar leyendo esos valores al mismo tiempo.

Para solucionar el problema se propone usar un solo objeto, bien de la clase `GestorHoraTemperatura`, o bien de la clase `GestorHoraTemperatura2`.

```java
public class GestorHoraTemperatura {
    private HoraTemperatura ht;

    public synchronized void almacenarHoraTemperatura(HoraTemperatura ht) {
        this.ht = ht;
    }

    public HoraTemperatura leerHoraTemperatura() {
        return ht;
    }
}

public class GestorHoraTemperatura2 {
    private static HoraTemperatura ht;

    public synchronized void almacenarHoraTemperatura(HoraTemperatura ht) {
        GestorHoraTemperatura2.ht = ht;
    }

    public synchronized static HoraTemperatura leerHoraTemperatura() {
        return ht;
    }
}

public class HoraTemperatura {
    private int hora; // en milisegundos
    private int temperatura; // en grados centígrados

    // Constructor
    public HoraTemperatura(int h, int t) {
        hora = h;
        temperatura = t;
    }

    // Getters y Setters
    // …
}
```

- (a) Para cada una de las dos soluciones propuestas, se pide responder si se conseguirá o no la sincronización deseada (una sola de las hebras del primer grupo, o cualquier número de hebras de las del segundo grupo), argumentando las respuestas.

??? note "Mostrar solución"
    Ninguna de las dos soluciones propuestas es correcta. En la primera de ellas, los procesos que escriben la temperatura y la hora (llamémosles "escritores") lo hacen en exclusión mutua entre ellos, lo cual es correcto, y los procesos que leen los valores (llamémosles "lectores") pueden estar cualquier número de ellos leyendo al mismo tiempo (al no estar el método de lectura sincronizado). Lo cual también coincide con lo que se desea.

    El problema de esta (pseudo)solución, sin embargo, es que también cualquier número de lectores pueden estar leyendo al mismo tiempo que un escritor escribe, lo cual es desde luego un comportamiento incorrecto.

    En la segunda solución propuesta, los lectores no pueden leer al mismo tiempo, ya que el método correspondiente está sincronizado. Lo cual está en contra de lo deseado. Además, al ser ahora la operación que hace la lectura un método de clase (estático), su exclusión mutua estará gobernada por el cerrojo de la clase, que es independiente de los cerrojos de los objetos de la clase, con lo que no ejecutará con exclusión mutua del otro método, el de escritura. Es decir, que puede haber un lector leyendo al mismo tiempo que un escritor escribiendo, lo cual es desde luego un comportamiento incorrecto. 
