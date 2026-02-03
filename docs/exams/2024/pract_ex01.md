---
id: ex-2024-01
year: 2024
exam: practicas
tags:
 - complejidad
---

- (a) (6 puntos) En relación al método getPuntuacionMediana, se quiere modificar con la siguiente signatura:

```java
/**
* Este método devuelve la mediana en el rango especificado en la lista
* ordenada de los tableros.
* @param min Número menor en el rango
* @param max Número mayor en el rango
* @return La mediana en el rango.
*/
public int getPuntuacionMediana(int min, int max){ . . .}
```

Notas:
    - Min y max se refieren a índices en la lista que se usa.
    - Suponga que los parámetros min y max que se reciben son válidos.

??? note "Mostrar solución"
    ```java
    public int getPuntuacionMediana(int min, int max) {
        // Se usa la división entera
        int mediana = (max + min) / 2;

        if ((mediana) % 2 == 0) {
            return tableros.get(mediana).getPuntuacion();
        } else {
            int pos1 = tableros.get(mediana).getPuntuacion();
            int pos2 = tableros.get(mediana + 1).getPuntuacion();
            // En estos casos, la mediana será un float. En este caso,
            // se utiliza la división entera, como indica la signatura.
            return (pos1 + pos2) / 2;
        }
    }
    ```
