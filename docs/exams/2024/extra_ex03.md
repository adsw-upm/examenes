---
id: ex-2024-03
year: 2024
exam: extraordinario
tags:
 - hebras
---

La pregunta consiste en simular la gestión de una gasolinera. La gasolinera tiene una cantidad limitada de surtidores y depósitos de diferentes tipos de combustibles (Gasolina y Diesel). Los vehículos y los camiones cisterna representan hebras que interactúan con la gasolinera y una taquilla de cobro/pago.

Monitor Gasolinera:
    - Controla el acceso a los surtidores y depósitos de combustible.
    - Se inicializa con un número de surtidores. Los depósitos se inicializan con 100 que será el tamaño máximo.
    - Permite la entrada de vehículos si hay surtidores disponibles.
    - Permite a los vehículos repostar si hay suficiente combustible en el depósito e inmediatamente después el vehículo sale de la gasolinera.
    - Permite a un camión cisterna rellenar un depósito si el nivel está por debajo del 10%, pero solo puede haber un camión repostando.

Monitor Taquilla:
    - Controla los pagos y cobros de la gasolinera y solo tiene una ventanilla para atender.
    - Permite que un vehículo pague por el combustible repostado y permite que un camión cisterna cobre por el combustible rellenado. Actualizando el dinero en caja.

Comportamiento de la hebra Vehículo:
    - Cada vehículo tiene un nombre y un tipo de combustible que usa. Un vehículo:
        - Entra en la gasolinera (si hay surtidores disponibles).
        - Reposta una cantidad específica de combustible y sale inmediatamente después.
        - Paga en la taquilla indicando el dinero a pagar.

Comportamiento de la hebra Camión Cisterna (no es un Vehículo):
    - Cada camión cisterna tiene un nombre y un tipo de combustible que puede rellenar.
    - Un camión cisterna:
        - Rellena un depósito de la gasolinera (si el nivel de combustible está por debajo del 10%).
        - Cobra en la taquilla indicando el dinero que debe cobrar.

Diagrama de clases:

![](./extra/extra_ex03.png)

Se pide:

Desarrolla el código del monitor Gasolinera:
- (a) (1 punto) Implementa el método
```java
public synchronized void entrar(String nombre) throws InterruptedException
```

??? note "Mostrar solución"
    FALTA.


- (b) (1,5 puntos) Implementa el método
```java
public synchronized void repostarYSalir(String nombre, Combustible tipo, int cantidad) throws InterruptedException
```

??? note "Mostrar solución"
    FALTA.



- (c) (1,5 puntos) Implementa el método 
```java
public synchronized void rellenarDeposito(String nombre, Combustible tipo, int cantidad) throws InterruptedException
```

??? note "Mostrar solución"
    FALTA.


Desarrolla el código del monitor Taquilla:

- (d) (0,5 puntos) Implementa el método
```java
public synchronized void pagar(String nombre, int cantidad, Combustible tipo) throws InterruptedException
```

??? note "Mostrar solución"
    FALTA.


- (e) (0,5 puntos) Implementa el método
```java
public synchronized void cobrar(String nombre, int cantidad, Combustible tipo) throws InterruptedException
```

??? note "Mostrar solución"
    FALTA.

