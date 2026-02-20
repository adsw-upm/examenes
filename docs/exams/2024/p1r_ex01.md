---
id: ex-2024-01
year: 2024
exam: parcial 1 recuperacion
tags:
 - complejidad
---

En esta asignatura se ha trabajado en la representación de las partidas
de ajedrez. Se pide desarrollar los siguientes métodos:

- (a) (1,5 puntos) `CompararTableros`:
```java
public boolean compararPiezas(Pieza p1, Pieza p2)
```

Este método comprueba si dos piezas coinciden: el mismo tipo y bando

|Parameters|
|---|
|`p1` - primera pieza para la comparación |
|`p2` - segundo pieza para la comparación |
|**Returns**o | 
| devuelve `true` si las piezas coinciden |

??? note "Mostrar solución"
    ```java
    public boolean compararPiezas(Pieza p1, Pieza p2) {
        if (p1 == null && p2 == null) {
            return true;
        }

        if (p1 != null && p2 != null) {
            if (p1.getTipo() == p2.getTipo()) {
                if (p1.getBando() == p2.getBando()) {
                    return true;
                }
            }
        }

        // Una de las piezas es null y la otra no
        return false;
    }
    ```


- (b) (1,5 puntos) `compararTableros`:

```java
public boolean compararTableros(Tablero t1, Tablero t2)
```

Este método comprueba si dos tableros coinciden: tienen que tener el mismo número de piezas y las mismas piezas en todas las posiciones.

|Parameters|
|---|
| `t1` - primer tablero para la comparación |
| `t2` - segundo tablero para la comparación |
| **Returns** |
| Devuelve `true` si los tableros coinciden |

??? note "Mostrar solución"
    ```java
    public boolean compararTableros(Tablero t1, Tablero t2) {
        Pieza[][] p1 = t1.getTablero();
        Pieza[][] p2 = t2.getTablero();
    
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (!compararPiezas(p1[i][j], p2[i][j])) {
                    return false;
                }
            }
        }
        return true;
    }
    ```


- (c) (2 puntos) `compararPartidas`
```java
public boolean compararPartidas(Partida p1, Partida p2)
```

Este método comprueba si dos partidas coinciden: tienen el mismo número de tableros, el mismo orden y los tableros coinciden

|Parameters|
|---|
| `p1` - primera partida para la comparación |
| `p2` - segunda partida para la comparación |
| **Returns** |
| Devuelve `true` si las partidas coinciden |

??? note "Mostrar solución"
    ```java
    public boolean compararPartidas(Partida p1, Partida p2) {
        if (p1.turnos.size() != p2.turnos.size()) {
            return false;
        }

        for (int i = 0; i < p1.turnos.size(); i++) {
            if (!compararTableros(p1.turnos.get(i), p2.turnos.get(i))) {
                return false;
            }
        }
        return true;
    }
    ```
    