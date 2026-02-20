---
id: ex-2024-02
year: 2024
exam: parcial 1 recuperacion
tags:
 - complejidad
---

Se desea implementar una estructura capaz de almacenar direcciones IP únicas y un algoritmo para consultar las direcciones almacenadas de manera eficiente. Esta estructura se basará en un árbol binario de búsqueda (BST). Dado que la aplicación que usa esta estructura será desplegada en un router empotrado, se decide almacenar el árbol en forma de array de tamaño fijo. Para ello, se procede de la siguiente manera. La posición `0` del array contendrá el nodo raíz. Dado un nodo en la posición `i`, su hijo izquierdo se encontrará en la posición `2*i+1`, y su hijo derecho en la posición `2*i+2`. Las posiciones con valor null corresponden a nodos que no existen en el BST. El siguiente es un ejemplo del estado del comienzo del array tras insertar 5 direcciones IP:

![](./p1r/p1r_ex02.png)

Se proporciona una clase `IP`, que representa direcciones IPv4. Esta clase implementa `Comparable` de manera adecuada y tiene un método `toString()` que devuelve la representación en texto de la IP. Además, se dispone del esqueleto de la clase, llamada `BSTSet`.

```java
public class BSTSet {
    private IP[] array;

    public BSTSet() {
        this.array = new IP[1023];
    }

    /**
     * Imprime todas las direcciones contenidas en el árbol, en
     * orden ascendente.
     */
    public void imprimir() {
        ...
    }

    /**
     * Devuelve true si la dirección especificada está en el árbol.
     * Complejidad: O(log(n)) con el tamaño del array.
     *
     * @param ip dirección a encontrar
     * @return true si la dirección ha sido encontrada
     */
    public boolean contains(IP ip) {
        ...
    }

    ...
}
```

Se pide:

- (a) (1.5 puntos) Desarrolle el método `imprimir()`, que muestre por pantalla todas las direcciones IP almacenadas en el BST en orden ascendente.

??? note "Mostrar solución"
    ```java
    /**
     * Imprime todas las direcciones contenidas en el árbol, en orden
     * ascendente.
     */
    public void imprimir() {
        imprimir(0);
    }

    private void imprimir(int pos) {
        if (pos >= this.array.length || this.array[pos] == null) {
            return;
        }

        imprimir(pos * 2 + 1);
        System.out.println(this.array[pos]);
        imprimir(pos * 2 + 2);
    }
    ```


- (b) (2.5 puntos) Desarrolle el método `contains(IP ip)`. Recuerde que el método debe tener un orden de complejidad $O(log(n))$, siendo $n$ el tamaño del array.

??? note "Mostrar solución"
    ```java
    public boolean contains(IP ip) {
        int pos = 0;

        while (pos < this.array.length) {
            IP actual = this.array[pos];

            if (actual == null) {
                return false;
            }

            int cmp = ip.cmp(actual);

            if (cmp == 0) {
                return true;
            } else if (cmp < 0) {
                pos = pos * 2 + 1;
            } else {
                pos = pos * 2 + 2;
            }
        }

        return false;
    }
    ```


- (c) (1 punto) ¿Cuál es la ocupación máxima del array (número máximo de direcciones IP que podrá almacenar) en esta implementación de BST si el nodo raíz contiene la dirección 0.0.0.1? Para una dirección IP del tipo A.B.C.D (con A, B, C y D entre 0 y 255), la implementación de `Comparable` compara los elementos A, B, C y D individualmente y en orden. Por ejemplo, la dirección 10.0.0.2 es menor que 10.0.0.3 y 10.0.1.1, pero mayor que 10.0.0.1.

??? note "Mostrar solución"
    Sabemos que al menos habrá 1 IP (la raíz). De los 1022 huecos restantes, dado que es un BST, supongamos que los huecos se dividen de forma igualitaria entre mayores (511) y menores (511). Sólo hay una posible posición menor (0.0.0.0), el resto (510) estarán vacías. Por tanto, dado que las IPs se insertan en el orden adecuado, la ocupación sería: 1 + 511 + 1 = 513 IPs.

    Ahora bien, nuestra suposición sólo se cumple si hay suficientes huecos para un árbol simétrico. Veamos cómo crece el número de posiciones en función de la profundidad:

    - A profundidad 0 hay 1 hueco y 1 posición.
    - A profundidad 1 habrá 2 huecos. Con un total de 1 + 2 = 3 posiciones.
    - A profundidad 2 habrá 4 huecos. Con un total de 3 + 4 = 7 posiciones.
    - A profundidad 3 habrá 8 huecos. Con un total de 7 + 8 = 15 posiciones.
    - A profundidad $k$ habrá $2ˆ(k+1)-1$ posiciones. Por lo que para $n$ posiciones: $n = 2(k+1)-1 \Rightarrow k = log_2(n+1) - 1$

    Por tanto, con 1023 posiciones habría espacio para 9 niveles completos de árbol binario.

    También podríamos concluir que, dado que cada nivel se rellena “de izquierda a derecha” (las posiciones más bajas son valores menores para cada nivel), la ocupación máxima en este caso sería igual hasta 1023+512=1535 huecos.
