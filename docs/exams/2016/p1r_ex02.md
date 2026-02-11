---
id: ex-2016-02
year: 2016
exam: parcial 1 recuperacion
tags:
 - ???
---

Una aplicación móvil registra la actividad de un senderista. Cuando empieza una caminata, la aplicación guarda la fecha (de comienzo del paseo) y una lista de coordenadas en el plano `(x, y)`, obtenidas cada segundo. Cuando el senderista termina su actividad, la aplicación manda a un servidor la siguiente información: nombre completo del senderista (`String`), fecha de comienzo de la actividad (`Date`) y la lista de coordenadas recorridas.

El servidor, escrito en Java, guarda para cada senderista, todas las rutas que haya recorrido. Para ello, dispone de un diccionario donde la clave es el nombre del senderista y el valor es una lista de todas las rutas recorridas por
dicho senderista.

Se dispone de las siguientes declaraciones:

```java
public class Coordenada {
    private double x, y;
    // constructor, getters y setters al uso

    public double distancia(Coordenada b) {
        int dx = Math.abs(x - b.x);
        int dy = Math.abs(y - b.y);
        return Math.sqrt(dx * dx + dy * dy);
    }
}

public class Servidor {
    private Diccionario rutas = new /* implementación */;

    public void anadir(String senderista, Ruta ruta) {
        // ...
    }

    public String campeon() {
        // ...
        return null;
    }
}

public class Ruta {
    private Date fechaComienzo;
    private List<Coordenada> puntos;
    // constructor, getters y setters al uso

    public double longitud() {
        // ...
        return 0.0;
    }
}
```

- (a) (1 punto) Codificar el método añadir.

??? note "Mostrar solución" 
    Como se usa un diccionario, es necesario que tengamos una lista de senderistas registrados. Por ello queda:
    ```java
    // rutas de cada senderista
    private Diccionario rutasPorSenderista = new DiccionarioHashMap(1000);
    // también vale:
    // private Map<String, List<Ruta>> rutasPorSenderista = new HashMap<>();

    // senderistas registrados, puede evitarse añadiendo keySet() a Diccionario
    private List<String> lsenderistas = new ArrayList<String>();

    public void anadir(String senderista, Ruta ruta) {
        List<Ruta> lr = (List<Ruta>) rutasPorSenderista.get(senderista);

        if (lr == null) { // senderista no registrado
            lsenderistas.add(senderista);
            lr = new ArrayList<Ruta>();
        }

        lr.add(ruta);
        rutasPorSenderista.put(senderista, lr);
    }
    ```


- (b) (1 punto) Codificar un método de la clase `Ruta` que calcule la longitud total del recorrido (método longitud de la clase `Ruta`).

??? note "Mostrar solución" 
    ```java
    public double longitud() {
        double total = 0;

        if (puntos == null || puntos.size() < 2) { // ¿no hay puntos?
            return 0;
        }

        Coordenada ant = puntos.get(0);
        for (int i = 1; i < puntos.size(); i++) {
            Coordenada sig = puntos.get(i);
            total += ant.distancia(sig);
            ant = sig;
        }

        return total;
    }
    ```


- (c) (2 puntos) Codificar un método de la clase `Servidor` que determine qué senderista ha recorrido más distancia en total, sumando todas sus rutas (método `campeon` de la clase `Servidor`). En caso de empate, puede devolver cualquiera.

??? note "Mostrar solución" 
    `campeon` usa un método auxiliar para averiguar la la suma de longitudes de las rutas de un usuario:
    ```java
    public String campeon() {
        String champ = null;
        double maxLong = -1;

        // también:
        // for (String senderista : rutasPorSenderista.keySet())
        for (String senderista : lsenderistas) {
            List<Ruta> lr = (List<Ruta>) rutasPorSenderista.get(senderista);
            double mayorCamino = sumaTotal(lr);

            if (mayorCamino > maxLong) {
                maxLong = mayorCamino;
                champ = senderista;
            }
        }
        return champ;
    }

    private double sumaTotal(List<Ruta> lr) {
        double suma = 0;
        for (Ruta r : lr)
            suma += r.longitud();
        return suma;
    }
    ```

