---
id: ex-2017-02
year: 2017
exam: extraordinario
tags:
 - complejidad
---

La clase RegistroDatos, permite almacenar los datos producidos por un conjunto de sensores. Los datos producidos por los sensores se envían como objetos de la clase Dato, cuya estructura se muestra a continuación:

```java
public class Dato implements Comparable<Dato> {

    private String id;   // Identificador único del sensor que ha generado el dato
    private Date d;      // Fecha en la que se ha producido el dato (clase Date de Java)
    private long v;      // Valor del dato producido
    ... //Contiene constructor, getters, y setters
}
```

La clase RegistroDatos guarda los datos recibidos en un array (private List<Dato> []datos). Cada dato se guarda en la posición del array que se obtiene aplicando el método hashCode de la clase String al identificador único del sensor que ha producido el dato y adaptando el resultado al tamaño del array datos. 

Además, se lleva una cuenta del número de datos que ha generado cada sensor, mediante el atributo cuentaDatos (private Map <String, Registro> cuentaDatos), usando como clave el identificador único del sensor que ha producido el dato y como valor un objeto de la clase Registro, cuya estructura se muestra a continuación:

```java
public class Registro implements Comparable<Registro> {

    private final String clave; // Identificador único del sensor
    private int cnt;            // Número de datos producidos por ese sensor
    ... //Contiene constructor, getters, y setters
}
```

- (a) (5 puntos) Se pide completar los métodos Constructor, put, getDatos, size y countAbove de la clase RegistroDatos. El esqueleto de la se muestra a continuación:

```java
public class RegistroDatos {
    private List<Dato>[] datos;
    private Map<String, Registro> cuentaDatos;

    /**
     * Constructor
     * @param n número de posiciones del array datos donde se van a almacenar
     * los datos producidos por los sensores
     */
    public RegistroDatos(int n) {
        //TODO
    }

    /**
     * Devuelve cuantos sensores han producido un número de datos por encima
     * de un determinado umbral c.
     * @param c umbral de cuenta.
     * @return número de sensores que han generado más de c datos
     */
    public int countAbove(int c) {
        //TODO
    }

    /**
     * Devuelve los datos producidos por un determinado sensor
     * @param sensorId identificador del sensor
     * @return lista de datos producidos por ese sensor.
     * Si no hay ningún sensor con ese sensorId devolverá una lista con 0 valores.
     */
    public List<Dato> getDatos(String sensorId) {
        //TODO
    }

    /**
     * Almacena un nuevo dato en el Registro de datos, para ello incrementa en uno la
     * cuenta de datos
     * proporcionados por el sensor, y almacena el dato en la posición correspondiente de
     * la tabla Hash
     * @param dato la nuevo dato a almacenar
     */
    private void put(Dato dato) {
        //TODO
    }

    /**
     * Numero de Datos total almacenado.
     * @return numero de datos.
     */
    public int size() {
        //TODO
    }
}
```

??? note "Mostrar solución"
    ```java
    public class RegistroDatos {
        private List<Dato>[] datos;
        private Map<String, Registro> cuentaDatos;

        /**
         * Constructor
         * @param n número de posiciones del array datos donde se van a almacenar
         * los datos producidos por los sensores
         */
        public RegistroDatos(int n) {
            this.datos = new List[N];
            for (int i = 0; i < N; i++) {
                datos[i] = new ArrayList();
            }
            cuentaDatos = new HashMap<String, Registro>();
        }

        /**
         * Devuelve cuantos sensores han producido un número de datos por encima
         * de un determinado umbral c.
         * @param c umbral de cuenta.
         * @return numero de sensores que han generado más de c datos
         */
        public int countAbove(int c) {
            int cuenta = 0;
            Set<String> keySet = cuentaDatos.keySet();
            for (String key : keySet) {
                if (cuentaDatos.get(key).getCnt() < c)
                    cuenta++;
            }
            return cuenta;
        }

        /*
         * Devuelve los datos producidos por un determinado sensor
         * @param sensorId identificador del sensor
         * @return lista de datos producidos por ese sensor.
         * Si no hay ningún sensor con ese sensorId devolverá una lista con 0 valores.
         */
        public List<Dato> getDatos(String sensorId) {
            List<Dato> listaDatos = new ArrayList<Dato>();
            int hc = sensorId.hashCode();
            hc = hc % datos.length;
            for (Dato d : datos[hc]) {
                if (d.getId().equals(sensorId))
                    listaDatos.add(d);
            }
            return listaDatos;
        }

        /**
         * El método put (), se encarga de meter un nuevo dato en el Registro de datos,
         * para ello incrementa en uno la cuenta de datos proporcionados por el sensor,
         * y almacena el dato en la posición correspondiente de la tabla Hash
         * @param dato la nuevo dato a almacenar
         */
        private void put(Dato dato) {
            if (cuentaDatos.containsKey(dato.getId())) {
                cuentaDatos.get(dato.getId()).inc();
            } else {
                cuentaDatos.put(dato.getId(), new Registro(dato.getId()));
            }
            int hc = dato.getId().hashCode();
            hc = hc % datos.length;
            datos[hc].add(dato);
        }

        /**
         * Numero de Datos Total Almacenado.
         * @return numero de datos.
         */
        public int size() {
            int suma = 0;
            Set<String> keySet = cuentaDatos.keySet();
            for (String key : keySet) {
                suma += cuentaDatos.get(key).getCnt();
            }
            return suma;
        }
    }
    ```

