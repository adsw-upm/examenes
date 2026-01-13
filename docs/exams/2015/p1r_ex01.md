---
id: ex-2015-01
year: 2015
exam: parcial 1 recuperacion
tags:
 - complejidad
---

Para un programa de análisis del genoma humano, necesitamos encontrar una subsecuencia de elementos en orden creciente. Esto corresponde a un problema de programación conocido como LIS (Longest Increasing Subsequence) donde, por ejemplo, dada la secuencia:

{0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15}

una solución (puede haber más de una) es:

[0, 2, 6, 9, 11, 15]

Buscando por Internet encontramos esta solución que hemos probado y pasa las pruebas:
```java
private class MyTouchListener implements OnTouchListener {
    private float x1;
    private float y1;

    public boolean onTouch(View view, MotionEvent event) {
        Movil jugador = terreno.getJugador();
        Juego juego = Juego.getInstance();
        if (jugador == null) {
            return false;
        }
        int action = event.getAction();
        switch (action) {
            case MotionEvent.ACTION_DOWN: {
                x1 = (int) (event.getX() / lado1);
                y1 = terreno.getN() - 1 – (int) event.getY() / lado1);
                Log.i(TAG, “Pulso en (“ + x1 + “ “ + y1 + “)”);
                return true;
            }
            case MotionEvent.ACTION_UP: {
                int x = (int) (event.getX() / lado1);
                int y = terreno.getN() - 1 – (int) event.getY() / lado1);
                if ((x != x1) || (y != y1)) {
                    Log.d(TAG, “No coinciden poner y quitar dedo”);
                    break;
                }
                if (x < terreno.getN() && y < terreno.getN()) {
                    if (terreno.getCasilla(x, y).getMovil() != null) {
                        Log.w(TAG, “Patito no puesto, ya hay otro móvil”);
                        break;
                    }
                    juego.pon(terreno.getCasilla(x, y), 0);
                    Log.d(TAG, "Patito puesto en (" + x + " " + y + ")");
                }
                break;
            }
            default:
        }
        return false;
    }
}
```

```java
int[] getLIS(int[] x) {
    int n = x.length;
    int[] len = new int[n];
    Arrays.fill(len, 1);
    int[] pred = new int[n];
    Arrays.fill(pred, -1);
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (x[j] < x[i] && len[i] < len[j] + 1) {
                len[i] = len[j] + 1;
                pred[i] = j;
            }
        }
    }
    int bi = 0;
    for (int i = 1; i < n; i++) {
        if (len[bi] < len[i])
            bi = i;
    }
    int cnt = len[bi];
    int[] res = new int[cnt];
    for (int i = bi; i != -1; i = pred[i])
        res[--cnt] = x[i];
    return res;
}
```

- (a) (4 puntos) Se pide calcular su complejidad en función del tamaño N de la secuencia de entrada, razonando la solución.

??? note "Mostrar solución"
    La iniciación de los arrays "len" y "pred" es de complejidad lineal, pues se visitan todos sus elementos una sola vez, y su longitud es n.

    A continuación hay un bucle doble anidado, cuyo cuerpo, de complejidad constante, se ejecuta 1 + 2 + 3 + ... + n-1 veces, es decir, un total de n/2*(n-1) veces. Por lo que su complejidad es cuadrática.

    Al final hay dos bucles simples con cuerpo de complejidad constante y número de vueltas de orden n, que tienen pues complejidad lineal.

    Sumando todas las complejidades individuales según su regla (el resultado es el término de mayor complejidad), la complejidad del algoritmo descrito resulta ser cuadrática. En términos formales:
    C(for.for) = O(1+2+3+...+(n-1)) = O(n/2 * (n-1)) = O(n^2 / 2) - O(n/2) = O(n^2)
    C(LIS) = C(arrays.fill) + C(Arrays.fill) + C(for.for) + C(for) + C(for)
    = O(n) + O(n) + C(for.for) + O(n) + O(n/k)
    = O(n) + O(n) + O(n^2) + O(n) + O(n)
    = O(n^2).