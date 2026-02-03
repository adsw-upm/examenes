---
id: ex-2024-05
year: 2024
exam: practicas
tags:
 - complejidad
---

En la práctica 2 empleábamos diferentes implementaciones de diccionarios para localizar la partida de un cierto tablero. En este ejercicio vamos a emplear la siguiente implementación de la clase Tablero y las siguientes pruebas JUnit. La implementación de Tablero será igual que teníamos en el enunciado o solución de la práctica, salvo lo que incluimos a continuación:

```java
1  public class Tablero {
2      // Resto es como enunciado/solución práctica
3      @Override
4      public boolean equals(Object obj) {
5          if (obj == null) {
6              return false;
7          }
8          if (obj instanceof Tablero) {
9              Tablero other = (Tablero) obj;
10             return
11                 this.representacion.equals(
12                     other.representacion);
13         }
14         return false;
15     }
16     @Override
17     public int hashCode() {
18         return 7;
19     }
20 }
```

```java
1  class TestTableroMap {
2      @Test
3      void test1() {
4          doTest("data/t1.txt");
5      }
6      @Test
7      void test2() {
8          doTest("data/t2.txt");
9      }
10     private void doTest(String file) {
11         try {
12             List<Partida> partidas =
13                 LectorPartidas.leerPartidas(file);
14             List<Tablero> tableros = new ArrayList<Tablero>();
15             Map<Tablero, Partida> tablero2Partida =
16                 new HashMap<Tablero, Partida>();
17             for (Partida partida : partidas) {
18                 tableros.addAll(partida.turnos);
19                 for (Tablero t : partida.turnos)
20                     tablero2Partida.put(t, partida);
21             }
22             assertEquals(tableros.size(),
23                          tablero2Partida.keySet().size());
24             for (Partida partida : partidas)
25                 for (Tablero t : partida.turnos)
26                     assertEquals(partida, tablero2Partida.get(t));
27         } catch (Exception e) {
28             fail();
29         }
30     }
31 }
```

Las pruebas que incluimos utilizan dos ficheros:
    - t1.txt: es un fichero con 5 partidas y cada partida 3 tableros. Los 15 tableros tienen todos representaciones de fichas deferentes.
    - t2.txt: es un fichero con 5 partidas y cada partida 3 tableros. Pero todas las partidas tienen un tablero con una representación de fichas iguales a otro tablero de otra partida.

Se pide:

- (a) (4 puntos) Con estas implementaciones de pruebas y Tablero, cuales de las pruebas fallan o tienen errores y cuales son pruebas correctas. Si la respuesta para alguna prueba es que falla o tiene error, justificar el motivo del fallo.

??? note "Mostrar Solución"
    Las dos pruebas comprueban que un tablero no remplaza a otro tablero en el mapa, y como todos los tablaros tienen el mismo hashCode, una clave remplaza a otro cuando dos claves son iguales. Las claves son iguales cuando las representaciones son iguales.

    t1.txt no tiene tableros con representaciones iguales. La prueba test1 no falla

    t2.txt tiene tableros con representaciones iguales. La prueba test2 falla.


- (b) (6 puntos) Cambiamos la línea 16 de las pruebas por la siguiente línea:
```java
new TreeMap<Tablero,Partida>();
```
Cambiar la clase Tablero para que las pruebas test1 y test2 funcionen correctamente. Se debe incluir cualquier cambio incluido en la solución de la práctica, que no estuviese incluido en el enunciado que incluía inicialmente la práctica, y que sean necesarios para que las dos pruebas funcionen.

??? note "Mostrar Solución"
    Para utilizar TreeMap Tablero tiene que implementar Comparable<Tablero> y los Tableros no pueden ser iguales cuando comparamos dos tableros. Actualizamos Tablero de la siguiente forma:
    ```java
    public class Tablero implements Comparable<Tablero> {
        private static int ID=0;
        private int id=ID++;
        @Override
        public int compareTo(Tablero o) {
            if (representacion.equals(o.representacion))
                return id-o.id;
            return representacion.compareTo(o.representacion);
        }
    }
    ```
    El orden de los tableros primero depende de la representación y para representación iguales del identificador de tablero. Con esta solución evitamos que el árbol esté desequilibrado, si fuse al revés e insertamos en el tablero en el mismo orden que creamos los tableros, quedaría desequilibrado.
