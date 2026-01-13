---
id: ex-2015-03
year: 2015
exam: extraordinario
tags:
 - monitores
---

- (a) (2 puntos) En el pacman presentado como proyecto 1, queremos modificar el comportamiento del Fantasma00 de forma que evite acercarse a los Depredadores. Los Depredadores no saben nada del asco que suscitan. Suponga que nos facilitan un método en Terreno que nos dice si hay un depredador a menos de 3 casillas de distancia de la que pasamos como argumento:

public synchronized boolean hayDepredador(Casilla casilla)

    - ¿Podemos hacerlo en el método run() de Fantasma00?Razone si sí o si no.
    - ¿Podemos hacerlo en el método puedoMoverme() de Fantasma00? Razone si sí o si no.
    - Si cree que se puede hacer de ambas maneras, indique ventajas e inconvenientes de una y otra opción

??? note "Mostrar solución"
    - Sí se puede en run().
    - Se puede optimizar el movimiento huyendo del depredador (moviendo en dirección opuesta).
    - Se ejecuta fuera de la zona crítica y el depredador y demás fantasmas se pueden mover mientras estamos eligiendo a dónde ir.
    - Sí se puede en puedoMoverme().
    - Sólo podemos hacer que el fantasma espere, sin moverse.
    - se ejecuta dentro de la zona crítica de forma que el depredador y todos los fantasmas están quietos mientras tomamos la decisión.