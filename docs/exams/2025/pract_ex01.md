---
id: ex-2025-01
year: 2025
exam: practicas
tags:
 - complejidad
---

En ajedrez, coronar un peón ocurre cuando un peón alcanza la última fila del tablero. Entonces, puede sustituir al peón por cualquier otra pieza, excepto el rey. Normalmente, la pieza elegida es la dama. 

- (a) (10 puntos) En este ejercicio, se pide desarrollar el método `sonVariasDamas`, con la siguiente signatura.
```java
public boolean sonVariasDamas(Tablero unTablero)
```

??? note "Mostrar solución"
    ```java
    public boolean sonVariasDamas(Tablero unTablero) {
    	Pieza[][] matrizPiezas = unTablero.getMatrizPiezas();
    	int nDamasBlancas = 0;
    	int nDamasNegras = 0;
    
    	for (int fila = 0; fila < 8; fila++) {
    		for (int columna = 0; columna < 8; columna++) {
    			Pieza pieza = matrizPiezas[fila][columna];
    			if (pieza != null) {
    				if (pieza.getTipo() == TipoPieza.REINA) {
    					if (pieza.getBando() == Bando.BLANCAS) {
    						nDamasBlancas ++;
    					} else {
    						nDamasNegras ++;
    					}
    				}
    			}
    		}
    	}
    	return nDamasBlancas > 1 || nDamasNegras > 1;
    }
    ```
