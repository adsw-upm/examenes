---
id: ex-2025-02
year: 2025
exam: extraordinario
tags:
 - complejidad
---

La multiplicación de números enteros grandes es costosa para los ordenadores, por lo que existen técnicas como el algoritmo de Karatsuba que hacen más eficiente este cálculo. El algoritmo de Karatsuba utiliza la técnica de divide y vencerás. Se basa en dividir los números a multiplicar en partes más pequeñas (más sencillas de manejar), operar sobre ellas y luego combinar los resultados para obtener el producto final. Por simplicidad, se asume que todas las operaciones se realizan con variables de tipo `int`.

Dados dos números enteros $x$ e $y$, se pueden representar como:

$x = a \cdot 10^n + b \hspace{3cm} y = c \cdot 10^n + d$

donde $a$, $b$, $c$ y $d$ son enteros, y $2n$ es el número total de dígitos que tienen tanto $x$ como $y$.

El algoritmo de Karatsuba nos indica que:

$x \cdot y = ac \cdot 10^{2n} + (ad + bc) \cdot 10^n + bd$

Esto se puede reescribir como:

$x \cdot y = z_1 \cdot 10^{2n} + z_2 \cdot 10^n + z_3$

donde $z_1 = ac$, $z_3 = bd$, $z_2 = (a + b)(c + d) - z_1 - z_3$

No es necesario para resolver el ejercicio. Para obtener $z_2$, partimos de la identidad $(a + b)(c + d) = ac + ad + bc + bd = z_1 + ad + bc + z_3$. Despejando, $ad + bc = (a + b)(c + d) - z_1 - z_3$, por tanto, $z_2 = ad + bc = (a + b)(c + d) - z_1 - z_3$.

Así, en lugar de realizar 4 multiplicaciones ($ac$, $ad$, $bc$, y $bd$), solo se hacen 3 multiplicaciones ($z_1$, $z_3$, y $(a+b)(c+d)$) y algunas operaciones más rápidas como sumas y restas. Esta idea se puede aplicar de forma recursiva, hasta que se multipliquen únicamente números de un solo dígito.

**Ejemplo**

Supongamos que se desea multiplicar los números $x = 56341032$ e $y = 72916764$. Primero, se dividen ambos números en dos partes:

* $x = 56341032 = 5634 \cdot 10^4 + 1032 \Rightarrow a = 5634,\, b = 1032$
* $y = 72916764 = 7291 \cdot 10^4 + 6764 \Rightarrow c = 7291,\, d = 6764$

Entonces, aplicamos la fórmula anterior:

* $z_1 = ac = 5634 \cdot 7291$
* $z_3 = bd = 1032 \cdot 6764$
* $z_2 = (a + b)(c + d) - z_1 - z_3 = (5634 + 1032)(7291 + 6764) - z_1 - z_3 = 6666 \cdot 14055 - z_1 - z_3$

Finalmente, el resultado se obtiene como:

$x \cdot y = z_1 \cdot 10^8 + z_2 \cdot 10^4 + z_3$

Para calcular $z_1$, $z_2$ y $z_3$, se aplicaría recursivamente el algoritmo de Karatsuba a las parejas:

$(5634, 7291)\hspace{2cm}(1032, 6764)\hspace{2cm}(6666, 14055)$


- (a) (1 punto) Razone cómo se aplicaría este algoritmo para multiplicar los números 34 y 78. ¿Cuántas veces debería llamarse al método `karatsuba(int x, int y)` y con qué parámetros?

??? note "Mostrar solución"
    Para multiplicar los números 34 y 78 utilizando el algoritmo de Karatsuba, primero dividimos ambos números en dos partes:
    
    * $x = 34 = 3 \cdot 10 + 4 \Rightarrow a = 3, b = 4$
    * $y = 78 = 7 \cdot 10 + 8 \Rightarrow c = 7, d = 8$
    
    Calculamos:
    
    * $z_1 = ac = 3 \cdot 7 \Rightarrow karatsuba(3,7) = 21$ 
    * $z_3 = bd = 4 \cdot 8 \Rightarrow karatsuba(4,8) = 32$
    * $z_2 = (a+b)(c+d) - z_1 - z_3 = (3 + 4)(7 + 8) - z_1 - z_3 = 7 \cdot 15 - z_1 - z_3 \Rightarrow karatsuba(7,15) = 105$
    

    Expandiendo `karatsuba(7,15)`:
    
    * $x = 7 = 0 \cdot 10 + 7 \Rightarrow a = 0, b = 7$
    * $y = 15 = 1 \cdot 10 + 5 \Rightarrow c = 1, d = 5$
    * $z_1 = ac = 0 \cdot 1 \Rightarrow karatsuba(0,1) = 0$ 
    * $z_3 = bd = 7 \cdot 5 \Rightarrow karatsuba(7,5) = 35$ 
    * $z_2 = (a+b)(c+d) - z_1 - z_3 = (0 + 7)(1 + 5) - z_1 - z_3 = 7 \cdot 6 - z_1 - z_3 \Rightarrow karatsuba(7,6) = 42$ 
    

    Con esto ya contestaríamos a la pregunta ya que tenemos todas las llamadas recursivas a `karatsuba`:

    $karatsuba(34,78) \hspace{1cm} karatsuba(3,7) \hspace{1cm} karatsuba(4,8) \hspace{1cm} karatsuba(7,15)$

    $karatsuba(0,1) \hspace{1cm} karatsuba(7,5) \hspace{1cm} karatsuba(7,6)$
    

    En total, se llama al método `karatsuba` 7 veces, la original más 6 llamadas recursivas.

    Si queremos completar el cálculo (no se pide en el ejercicio), reconstruimos primero $karatsuba(7,15)$ como:

    - $z_2 = 42 - 35 = 7$
    - $7 \cdot 15 = z_1\cdot 100 + z_2 \cdot 10 + z_3 = 0 \cdot 100 + 7 \cdot 10 + 35 = 0 + 70 + 35 = 105$

    Finalmente, reconstruimos el resultado de la multiplicación original:

    - $z_2 = 105 - 21 - 32 = 52$
    - $34 \cdot 78 = z_1 \cdot 100 + z_2 \cdot 10 + z_3 = 21 \cdot 100 + 52 \cdot 10 + 32 = 2100 + 520 + 32 = 2652$


- (b) (2 puntos) Realice una implementación del algoritmo de Karatsuba en Java. Para ello, implemente un método `karatsuba` que reciba como parámetros dos números enteros `x` e `y` y devuelva el resultado de la multiplicación utilizando dicho algoritmo. La cabecera del método es `public int karatsuba(int x, int y)`.
El método no puede realizar multiplicaciones de números de más de un dígito y todas las multiplicaciones se realizan utilizando el algoritmo de Karatsuba. Se asume que los números `x` e `y`, con los que se invoca inicialmente el método, tendrán el mismo número de dígitos. Suponga que existen los siguientes métodos auxiliares:

    - `static int[] splitint(int num, int digitos)` que recibe un número entero `num` y un número de dígitos. El método parte el número `num` en dos partes de `digitos` dígitos cada una y devuelve un array con las dos partes. Por ejemplo, si `num = 12345678` y `digitos = 4`, el método devolverá el array `[1234, 5678]`. El método rellena con ceros a la izquierda si es necesario. Si `num = 123` y `digitos = 2`, el método devolverá el array `[01, 23]`.
    -  `static int length(int num)` que recibe un número entero `num` y devuelve el número de dígitos que tiene. Por ejemplo, si `num = 12345`, el método devolverá `5`.
    -  `static int pow10(int num, int exp)` que recibe un número entero `num` y un exponente `exp`, y devuelve como resultado `num` con `exp` ceros a la izquierda. Por ejemplo, si `num = 123` y `exp = 2`, el método devolverá `12300`.

??? note "Mostrar solución"
    Implementación en Java:

    ```{.java .numberLines}
    public static int karatsuba(int x, int y) {
      if (x < 10 && y < 10) {
        return x * y;
      }

      int n = (Math.max(length(x), length(y))+1) / 2; // Redondeamos hacia arriba para dividir en dos partes

      int[] xParts = splitint(x, n);
      int[] yParts = splitint(y, n);
      int a = xParts[0];
      int b = xParts[1];
      int c = yParts[0];
      int d = yParts[1];

      int z1 = karatsuba(a, c);
      int z3 = karatsuba(b, d);
      int z2 = karatsuba(a + b, c + d) - z1 - z3;

      return z1 * pow10(1, 2 * n) + z2 * pow10(1, n) + z3;
    }
    ```


- (c) (2 puntos) En este tipo de algoritmos recursivos, es común que se realicen múltiples llamadas al mismo método con los mismos parámetros. Una forma de optimizar estos algoritmos es añadir una cache para evitar estos cálculos repetidos. Esto significa que, si se llama al método `karatsuba` con los mismos parámetros que en una llamada anterior, se devolverá el resultado ya calculado en lugar de volver a calcularlo. Sin repetir el código del método del apartado anterior, indique que modificaciones haría para implementar esta cache. Nota: No es necesario preocuparse por posibles desbordamientos del tipo `int`. Se asume que los casos de prueba no excederán su límite.

??? note "Mostrar solución"
    Para implementar una cache, se puede utilizar un `Map` para almacenar los resultados ya calculados. Aquí está la modificación del método `karatsuba`:

    ```{.java .numberLines}
      // Fuera del método
      private static Map<String, Integer> cache = new HashMap<>();

      public static int karatsuba(int x, int y) {
        String key = x + "," + y;
        if (cache.containsKey(key)) {
          return cache.get(key);
        }

        // el resto del código es igual al anterior

        cache.put(key, result); 
        return result;
      }

    ```

