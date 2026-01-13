---
id: ex-2015-02
year: 2015
exam: parcial 1 recuperacion
tags:
 - ???
---

Dado el siguiente terreno de prueba y la situación del jugador y el depredador que se muestra:

![](./p1r/p1r_ex03.png)

- (a) (1 punto) Describa un caso posible de error para detectar errores del método primerPaso de la clase Depredador del alumno y prográmelo con JUnit.
??? note "Mostar solución"
    Suponemos que la variable terreno se refiere al terreno creado con la configuración de la figura, y que la variable depredador se refiere al depredador situado en el terreno anterior.

    El primer paso de la ruta más corta desde la casilla donde está el depredador (1,1) y la del jugador (3,2) es la casilla (1,0). Para comprobar que el funcionamiento del método primerPaso() es correcto, pues, basta con probar la siguiente aserción
    
    assertEquals(terreno.getCasilla(1,0),
    
    depredador.primerPaso(terreno.getCasilla(1,1),terreno.getCasilla(3,2)))

- (b) (1 punto) Escriba un caso de prueba para comprobar si el número de paredes en el terreno es igual a 10 (los bordes no cuentan), utilizando métodos públicos de las clases del proyecto.

??? note "Mostar solución"
    Para comprobar el número de paredes basta hacer
        assertEquals(10, terreno.getparedes().size()