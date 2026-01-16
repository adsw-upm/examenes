---
id: ex-2017-01
year: 2017
exam: parcial 1
tags:
 - complejidad
---

Sabiendo que el tiempo de ejecución de la función f es constante y el de g es lineal con respecto a n.

- (a) (1,65 puntos) Razone la complejidad de: 
```java
for (int i = 1; i < n; i++) {
    f(i);   
};
```

??? note "Mostrar solución"
El bucle se ejecuta n veces, y el tiempo de ejecución de f es constante, por lo que la complejidad es n*O(1) = O(n).


- (b) (1,65 puntos) Razone la complejidad de: 
```java
for (int i = 1; i < n; i++) {
    g(i);
};
```
??? note "Mostrar solución"
    Este bucle se ejecuta n veces, pero ahora el tiempo de ejecución de g es lineal respecto a n. Por tanto, la complejidad es N*O(N) = O(n2).


- (c) (1,65 puntos) Rrazone la complejidad de: 
```java
for (int i = 1; i < n; i++) {
    for (int j = 1; j < i; j*=2) {
        f(j);
    };
};
```
??? note "Mostrar solución"
    El bucle exterior se ejecuta n veces, y el bucle interior se ejecuta log i veces. El tiempo de ejecución de f es constante, como antes. Por tanto la complejidad es O (N log N).
