---
id: ex-2015-02
year: 2015
exam: parcial 1 recuperacion
tags:
 - monitores
---

Se tiene un sistema con dos hebras (H1 y H2) que acceden continuamente a un recurso compartido, que se debe usar con exclusión mutua. Para que el sistema funcione correctamente las hebras tienen que acceder según el siguiente patrón, que se  debe repetir cíclicamente: H1, H1, H2, H1, H2, como se ve en la figura siguiente:

![](./p1r/p1r_ex02.png)

- (a) (4 puntos) Se pide desarrollar el monitor (GestorCiclosAcceso) para sincronizar las hebras según el comportamiento descrito. El monitor debe proporcionar las siguientes operaciones:
    - ... void accederH1(): Este método lo invoca la hebra H1 para solicitar acceso al recurso compartido.
    - ... void accederH2(): Este método lo invoca la hebra H2 para solicitar acceso al recurso compartido.
    - ... void liberar(): Este método lo invocan las hebras para liberar el recurso compartido.

??? note "Mostrar solución"
    ```java
    public class GestorCiclosAcceso {
        private boolean turnoH1 = true;
        private int nAccesoH1 = 0;
        private int nAccesoCicloH1 = 3;
        private boolean recursoOcupado = false;
    
        public synchronized void accederH1()
                throws InterruptedException {
            while (!turnoH1 || recursoOcupado)
                wait();
            if (nAccesoH1 == 0)
                turnoH1 = true;
            else
                turnoH1 = false;
            nAccesoH1++;
            if (nAccesoH1 == nAccesoCicloH1)
                nAccesoH1 = 0;
            recursoOcupado = true;
        }
    
        public synchronized void accederH2()
                throws InterruptedException {
            while (turnoH1 || recursoOcupado)
                wait();
            turnoH1 = true;
            recursoOcupado = true;
        }
    
        public synchronized void liberar()
                throws InterruptedException {
            recursoOcupado = false;
            notifyAll();
        }
    }
    public class GestorCiclosAcceso {
        private boolean turnoH1 = true;
        private int nAccesoH1 = 0;
        private int nAccesoCicloH1 = 3;
        private boolean recursoOcupado = false;
    
        public synchronized void accederH1()
                throws InterruptedException {
            while (!turnoH1 || recursoOcupado)
                wait();
            if (nAccesoH1 == 0)
                turnoH1 = true;
            else
                turnoH1 = false;
            nAccesoH1++;
            if (nAccesoH1 == nAccesoCicloH1)
                nAccesoH1 = 0;
            recursoOcupado = true;
        }
    
        public synchronized void accederH2()
                throws InterruptedException {
            while (turnoH1 || recursoOcupado)
                wait();
            turnoH1 = true;
            recursoOcupado = true;
        }
    
        public synchronized void liberar()
                throws InterruptedException {
            recursoOcupado = false;
            notifyAll();
        }
    }
    ```
    Otra posible implementación, que utiliza máquinas de estados, es la siguiente:
    
    ```java
    public class GestorCiclosAcceso2 {
        // estado 0 - espera H1
        // estado 1 - espera H1
        // estado 2 - espera H2
        // estado 3 - espera H1
        // estado 4 - espera H2
        private int state = 0;
        private boolean busy = false;
    
        public synchronized void accederH1()
                throws InterruptedException {
            while (busy || !espera(1))
                wait();
            busy = true;
            state = (state + 1) % 5;
        }
    
        public synchronized void accederH2()
                throws InterruptedException {
            while (busy || !espera(2))
                wait();
            busy = true;
            state = (state + 1) % 5;
        }
    
        public synchronized void liberar()
                throws InterruptedException {
            busy = false;
            notifyAll();
        }
    
        private boolean espera(int i) {
            switch (state) {
                case 0:
                case 1:
                case 3:
                    return i == 1;
                case 2:
                case 4:
                    return i == 2;
            }
            return false;
        }
    }
    ```

