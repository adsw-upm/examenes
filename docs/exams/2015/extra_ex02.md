---
id: ex-2015-02
year: 2015
exam: extraordinario
tags:
 - monitores
---

Un sistema está compuesto por un conjunto de hebras que deben acceder a un recurso compartido con exclusión mutua. Estas hebras se dividen en dos grupos: H1 y H2. Las hebras del grupo H2 acceden al recurso con prioridad respecto a las del grupo H1. Es decir, las hebras H1 no pueden acceder al recurso si hay alguna hebra H2 esperando. Además, las hebras del grupo H1 deben acceder al recurso en el mismo orden en el que lo han solicitado.

- (a) (4 puntos) Se pide desarrollar el monitor GestorRecurso que gestione el acceso al recurso, de acuerdo a las características descritas. El monitor deberá tener tres operaciones:
    - … solicitarRecursoH1(): Este método lo invocan las hebras del grupo H1 para solicitar acceso al recurso.
    - … solicitarRecursoH2(): Este método lo invocan las hebras del grupo H2 para solicitar acceso al recurso.
    - … liberarRecurso(): Este método lo invocan las hebras de los dos grupos para liberar el recurso.

??? note "Mostrar solución"
    ```java
    public class GestorRecurso {
        private int turno = 0;
        private int ultimoSolicitar = 0;
        private int nH2Esperando = 0;
        private boolean recursoOcupado = false;
    
        public synchronized void SolicitarRecursoH1() throws InterruptedException {
            int miTurno = ultimoSolicitar;
            ultimoSolicitar++;
            while (miTurno > turno || nH2Esperando > 0 || recursoOcupado) {
                wait();
            }
            turno++;
            recursoOcupado = true;
        }
    
        public synchronized void SolicitarRecursoH2() throws InterruptedException {
            nH2Esperando++;
            while (recursoOcupado) {
                wait();
            }
            recursoOcupado = true;
            nH2Esperando--;
        }
    
        public synchronized void LiberarRecurso() {
            recursoOcupado = false;
            notifyAll();
        }
    }
    ```