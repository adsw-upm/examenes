---
id: ex-2024-04
year: 2024
exam: practicas
tags:
 - grafos
---

- (a) (4 puntos) Modifique el método getTablerosConPuntuacionMinima para convertirlo en getTablerosConPuntuacionMaxima, que devuelva todos los tableros que tengan una puntuación igual o inferior a la que se pase como parámetro.

```java
public List<Tablero> getTablerosConPuntuacionMaxima(int puntuacion)
```

??? note "Mostrar solución"
    ```java
    public List<Tablero> getTablerosConPuntuacionMaxima(int puntuacion) {
        int posicion = tableros.size();
        for (int i = 0; i < tableros.size(); i++) {
            if (tableros.get(i).getPuntuacion() > puntuacion) {
                posicion = i;
                break;
            }
        }
        return tableros.subList(0, posicion);
    }
    ```
