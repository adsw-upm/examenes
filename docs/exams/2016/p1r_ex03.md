---
id: ex-2016-03
year: 2016
exam: parcial 1 recuperacion
tags:
 - monitores
---

Sea un un sistema de gestión de turnos en un supermercado. Los usuarios, con el teléfono inteligente, piden número al gestor de turnos, y pueden preguntar en cualquier momento por el turno actual. Los dependientes, con
unos botones que hay en los mostradores, hacen avanzar el turno actual.

Hay un gestor central que coordina las peticiones y avances para que no haya duplicidades ni se pierda ningún turno. Su esquema es:

```java
class Gestor {
    // devuelve turnos correlativos 1, 2, 3, ...
    public int getTurno() { … }

    // avanza el turno al número siguiente
    public void avanzaTurno() { … }

    // dice en qué turno estamos
    public int getActual() { … }
}
```

- (a) (1,5 puntos) Complete la clase Gestor, teniendo en cuenta que debe poder recibir llamadas concurrentes de clientes y dependientes.

??? note "Mostrar solución"
    public class Gestor {
        private int turno = 0;
        private int actual = 0;

        // devuelve turnos correlativos 1, 2, 3, ...
        public synchronized int getTurno() {
            turno++;
            return turno;
        }

        // avanza el turno al número siguiente
        public synchronized void avanzaTurno() {
            if (actual <= turno)
                actual++;
        }

        // dice en qué turno estamos
        public synchronized int getActual() {
            return actual;
        }
    }


- (b) (1,5 puntos) Escriba el código de una clase Cliente que defina una hebra (thread) que efectúe las siguientes operaciones: 
    – Pide turno
    – Cada 10 s consulta el turno actual
    – Si faltan menos de 5 turnos hace BIP()
    – Si le toca el turno hace BIP(); BIP();
    – Si se ha pasado el turno termina la ejecución de la hebra

NOTAS:
1. Suponga que el método BIP() está disponible directamente en la plataforma de ejecución
2. El método avanzaTurno no debe incrementar el número de turno más allá del último número emitido. Por
ejemplo, si el último número devuelto por getTurno es el 41, el método avanzaTurno puede llegar a 42,
pero no puede avanzar a 43.
3. Los métodos de Gestor devuelven el control inmediatamente, sin esperas.

??? note "Mostrar solución"
    public class Cliente extends Thread {
        private Gestor gestor;
    
        public Cliente(int id, Gestor gestor) {
            this.gestor = gestor;
        }
    
        @Override
        public void run() {
            int turno = gestor.getTurno();
            int actual;
    
            do {
                actual = gestor.getActual();
    
                if (turno - actual < 5)
                    BIP();
    
                if (actual == turno) {
                    BIP();
                    break;
                }
    
                try {
                    sleep(10000);
                } catch (InterruptedException ignored) {
                }
    
            } while (turno > actual);
        }
    }
    
