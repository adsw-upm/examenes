---
id: ex-2017-01
year: 2017
exam: extraordinario
tags:
 - ???
---

Varios ingenieros utilizan una base de datos para almacenar informes. Para ello disponen de una aplicación que permite almacenar un informe o recuperar un informe anterior. El acceso a los datos se organiza mediante una clase de Java que responde al esquema siguiente esquema:

```java
public class Datos {
…
    public … void guardar (String clave) {…}
    public … void consultar (String clave) {…}
    public … void terminar (String clave) {…}
}
```

Las aplicaciones se ejecutan concurrentemente, y llaman a guardar o a consultar antes de realizar una secuencia de operaciones de almacenar o recuperar informes, respectivamente. Cuando han terminado de realizar estas operaciones llaman a terminar. Puede haber varias aplicaciones consultando informes a la vez, pero no consultando y guardando, ni varias guardando a la vez.

Los objetos de la clase Ingeniero son hebras que ejecutan repetidamente el siguiente código:

```java
datos.guardar(clave);
for (int i = 1; i <= ndoc; i++) {
    // generar informe y almacenarlo en la base de datos
}
datos.terminar(clave);
```

o bien

```java
datos.consultar(clave);
for (int i = 1; i <= ndoc; i++) {
    // realizar consulta en la base de datos
}
datos.terminar(clave);
```

- (a) (4 puntos) Complete el código de la clase Datos de forma que se cumplan las condiciones del enunciado.

??? note "Mostrar solución"
    ```java
    public class Datos {
        private int consultando = 0;
        private boolean guardando = false;
    
        public synchronized void guardar(String clave) {
            while (guardando || consultando > 0)
                try {
                    wait();
                } catch (InterruptedException e) {}
            guardando = true;
        }
    
        public synchronized void consultar(String clave) {
            while (guardando)
                try {
                    wait();
                } catch (InterruptedException e) {}
            consultando++;
        }
    
        public synchronized void terminar(String clave) {
            if (consultando > 0) {
                consultando--;
            } else {
                guardando = false;
            }
            notifyAll();
        }
    }
    ```


- (b) (2 puntos) Escriba el código de una posible implementación de la clase Ingeniero para consultar datos.


??? note "Mostrar solución"
    ```java
    public class Ingeniero_Consulta extends Thread {
        Datos datos;
        int ndoc = 10; // por ejemplo

        public Ingeniero_Consulta(Datos datos) {
            this.datos = datos;
        }

        public void run() {
            datos.consultar("clave"); // por ejemplo
            for (int i = 1; i <= ndoc; i++) {
                // realizar la consulta
            }
            datos.terminar("clave");
        }
    }
    ```


- (c) (2 puntos) Analice si puede haber problemas de inanición (starvation) en el acceso a los datos y, si es así, ponga algún ejemplo (sin resolverlo).

??? note "Mostrar solución"
    Como en el problema original, la solución dada puede dar lugar a inanición de los ingenieros que guardan informes. Por ejemplo, sin entran varios a consultar y antes de que terminen entran otros nuevos, esta situación se puede prolongar indefinidamente, no dejando acceder nunca a otros ingenieros que deseen guardar informes. Las solución es establecer turnos para dar prioridad, alternativamente, a los que guardan (escritores) y a los que consultan (lectores)

