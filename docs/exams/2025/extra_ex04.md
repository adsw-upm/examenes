---
id: ex-2025-04
year: 2025
exam: extraordinario
tags:
 - complejidad
---

Se dispone de un grafo no dirigido que relaciona ciudades y las personas que han viajado entre ellas.

* Nodo representa a una ciudad.
* Arista representa a una persona que ha realizado un viaje entre dos ciudades.

En el grafo no existe más de una arista entre las mismas dos ciudades con la misma persona.

![](extra/extra_ex04.png)

- (a) (5 puntos) Se pide implementar el siguiente método:

```{.java .numberLines}
/**
 * Devuelve una lista con todas las ciudades que ha visitado la persona cuyo
 * nombre se pasa por parámetro.
 * El resultado no debe contener ciudades repetidas.
 *
 * @param nombre Nombre de la persona de la que se quiere saber qué ciudades ha visitado.
 * @param grafo Grafo no dirigido que modela los viajes.
 * @return Lista de nombres de ciudades visitadas (sin repeticiones).
 */
public List<String> ciudadesDePersona(String nombre, GrafoNoDirigido grafo)
```

??? note "Mostrar solución"
    ```{.java .numberLines}
    import java.util.ArrayList;
    import java.util.List;
    import java.util.Set;

    public class CiudadesDePersona {

        /**
         * Genera una lista de las ciudades que ha visitado la persona indicada,
         * sin ciudades repetidas.
         *
         * @param nombre nombre de la persona
         * @param grafo  grafo de ciudades y viajes
         * @return lista (sin repeticiones) de ciudades visitadas
         */
        public List<String> ciudadesDePersona(String nombre, GrafoNoDirigido grafo) {

            List<String> listaCiudades = new ArrayList<>();
            Set<Nodo> nodos = grafo.getNodos();

            for (Nodo nodo : nodos) {
                for (EnlaceNoDirigido enlace : nodo.getEnlaces()) {
                    if (nombre.equals(enlace.getPersona().getNombre())) {
                        /* Añadimos ambas ciudades del viaje */
                        addCiudad(enlace.getUno(), listaCiudades);
                        addCiudad(enlace.getOtro(enlace.getUno()), listaCiudades);
                    }
                }
            }
            return listaCiudades;
        }

        /** Añade la ciudad del nodo si todavía no está en la lista. */
        private void addCiudad(Nodo nodo, List<String> lista) {
            String ciudad = nodo.getCiudad();
            if (!lista.contains(ciudad)) {
                lista.add(ciudad);
            }
        }
    }
    ```
