---
id: ex-2024-03
year: 2024
exam: practicas
tags:
 - hebras
---

- (a) (6 puntos) Desarrolle el método getPorcentajeTablerosConVentaja(Bando bando) en la clase GestorTableros. Este método debe devolver un número decimal que represente el tanto por ciento de tableros en que el bando que se pasa como parámetro tiene una puntuación superior al bando contrario.
```java
public double getPorcentajeTablerosConVentaja(Bando bando)
```

??? note "Mostrar Solución"
    ```java
    public double getPorcentajeTablerosConVentaja(Bando bando) {
        return getTablerosConVentaja(bando) / tableros.size();
    }

    public List<Tablero> getTablerosConVentaja(Bando bando) {
        Bando contrario;
        if (bando == Bando.BLANCAS) {
            contrario = Bando.NEGRAS;
        } else {
            contrario = Bando.BLANCAS;
        }

        List<Tablero> tablerosConVentaja = new ArrayList<>();
        for (Tablero tablero : tableros) {
            if (tablero.getPuntuacionBando(bando) > tablero.getPuntuacionBando(contrario)) {
                tablerosConVentaja.add(tablero);
            }
        }

        return tablerosConVentaja;
    }
    ```
