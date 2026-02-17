---
id: ex-2018-05
year: 2018
exam: extraordinario
tags:
 - monitores
---

Se desea ampliar el juego de la serpiente con un contador de las manzanas que ha comido la serpiente. Naturalmente, cuando la serpiente come una manzana, este contador debe aumentar en una unidad. Para añadir dificultad al jugador, también puede perder manzanas de este contador por dos motivos:

- Si una bola choca con una manzana, el jugador pierde una unidad de su contador de manzanas comidas. El contador no puede nunca tener un valor inferior a cero como resultado de esta pérdida, pero la pérdida debe ejecutarse tan pronto como sea posible;
- Si la serpiente es golpeada en la cabeza por una bola, el contador de manzanas se reduce a la mitad, redondeando al entero inmediatamente inferior. Esto es, si el jugador tenía 7 puntos debe quedarse con 3.

Siendo la clase `Manzanas`:
```java
public class Manzanas
implements Screen.Thing {

    /** Constructor. */
    public Manzanas() {
        font = new Font("SansSerif", Font.BOLD, 18);
        Game.getScreen().add(this);
    }

    /** La serpiente ha comido una manzana. */
    public void appleEaten() {
    }

    /** Una bola ha destruido una manzana. */
    public void appleDestroid() {
    }

    /** Una bola ha golpeado la cabeza de la serpiente. */
    public void headShot() {
    }

    /** Se imprime en pantalla. */
    @Override
    public void paint(Graphics2D g) {
        g.setFont(font);
        g.setColor(Color.BLACK);
        g.drawString("manzanas: " + , 10, 30);
    }
}
```

- (a) (5 puntos) Se pide que complete y modifique la clase monitor `Manzanas` como considere oportuno para obtener la funcionalidad descrita.

??? note "Mostrar solución"
    ```java
    /**
     * Contador de manzanas.
     */
    public class Manzanas
    implements Screen.Thing {
    
        private int manzanas;
    
        public Manzanas() {
            font = new Font("SansSerif", Font.BOLD, 18);
            manzanas = 0;
            Game.getScreen().add(this);
        }
    
        public synchronized void appleEaten() {
            manzanas++;
            notifyAll();
        }
    
        public synchronized void appleDestroid() {
            while (manzanas <= 0) {
                try {
                    wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            manzanas--;
        }
    
        public synchronized void headShot() {
            manzanas = manzanas / 2;
        }
    
        @Override
        public void paint(Graphics2D g) {
            g.setFont(font);
            g.setColor(Color.BLACK);
            g.drawString("manzanas: " + manzanas, 10, 30);
        }
    }
    ```
