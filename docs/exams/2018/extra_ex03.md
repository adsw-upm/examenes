---
id: ex-2018-03
year: 2018
exam: extraordinario
tags:
 - hebras
---

- (a) (2 puntos) Explique brevemente cuál es la diferencia entre interbloqueo (*deadlock*) y bloqueo vivo (*livelock*).

??? note "Mostrar solución"
    En un interbloqueo hay varias hebras suspendidas, esperando conseguir recursos que tienen que liberar otras hebras, de tal manera que en conjunto se forma una cada de espera circular y ninguna hebra puede avanzar.

    En un bloqueo vivo hay igualmente varias hebras intentando conseguir recursos que tienen otras hebras. La diferencia es que cuando una hebra no puede conseguir todos sus recursos libera los que tiene y lo vuelve a intentar. Como consecuencia, las hebras implicadas están continuamente activas, aunque sin realizar ningún progreso.

    Por tanto, la diferencia fundamental es que en un interbloqueo las hebras estás suspendidas y nunca se ejecutan, mientras que en un bloqueo vivo las hebras se ejecutan pero no progresan.


Sea un sistema con 8 GB de memoria principal. Tenemos procesos concurrentes que solicitan memoria en bloques de 2 GB a medida que la necesitan para su ejecución. Un proceso que ya tiene `N` bloques de memoria asignados puede solicitar más memoria, y si ya no hay memoria disponible espera a que la haya antes de continuar. La memoria asignada a un proceso se libera completamente cuando el proceso termina su ejecución.

- (b) (3 puntos) Indique razonadamente si es posible que se dé una situación de interbloqueo (*deadlock*), en qué circunstancias podría ocurrir y, si éste es el caso, cómo se podría evitar.

??? note "Mostrar solución"
    Los procesos acceden a un conjunto de recursos, los bloques de memoria, todos iguales, con una disponibilidad total limitada a 4 bloques en total. Se pueden producir interbloqueos si varios procesos intentan adquirir más memoria cuando ya está toda asignada a otros procesos que también necesitan más memoria.

    Por ejemplo, supóngase que hay dos procesos `P` y `Q`, que tiene asignados 2 bloques de memoria cada uno, es decir 4 en total, por lo que no hay bloques libres. Si ambos solicitan un bloque adicional cada uno, al no estar disponible se suspenden esperando que haya memoria libre. Para ello uno de los dos tendría que terminar, liberando su memoria, pero al no poder avanzar ninguno de los dos se quedan suspendidos indefinidamente.

    Podemos comprobar que se cumplen las condiciones necesarias de Coffman:

    1. Exclusión mutua: Un bloque de memoria sólo puede estar asignado a un proceso.
    2. Tener y esperar: Un proceso puede tener asignada memoria y esperar que conseguir más.
    3. Sin expulsión: No se quita memoria a un proceso hasta que termina su ejecución.
    4. Espera circular, como pone de manifiesto el ejemplo anterior.

    Para evitar el interbloqueo la solución más sencilla sería obligar a que los procesos soliciten toda la memoria que pueden necesitar al iniciarse, invalidando la condición 2. Nótese que la solución frecuentemente recomendada de asignar los recursos siempre en el mismo orden no es aplicable aquí porque todos los bloques de memoria son iguales

