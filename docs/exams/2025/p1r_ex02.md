---
id: ex-2025-02
year: 2025
exam: parcial 1 recuperacion
tags:
 - complejidad
---

En un sistema de gestión de la información de personas, se quieren implementar los métodos que se describen a continuación. Se pide:

- (a) (2,5 puntos)  El sistema proporciona el método `personasEnCiudad`, que permite obtener la lista de las personas de una ciudad. El número de accesos a este método es muy elevado, por lo que es importante tener una respuesta muy eficiente. Para ello, se pide determinar una estructura de datos en la clase adecuada para satisfacer este requisito. Justifique brevemente su decisión y desarrolle el código necesario para crear la estructura de datos seleccionada e implementar el método `personasEnCiudad`. 

- (b) (2,5 puntos) Se quiere obtener una lista de las ciudades que tengan el mayor número de personas con un nombre. En este caso no es crítico el rendimiento, pero se considerará su comportamiento. 

Documentación de la clase `GestorPersonas`
```java
/**
 * Constructor de la clase GestorPersonas
 * 
 * @param arrayPersonas array con todas las personas
 */
public GestorPersonas(Persona[] arrayPersonas)

/**
 * Retorna una lista de las personas en una ciudad.
 * 
 * @param ciudad la ciudad para la búsqueda
 * @return una lista con las personas en esa ciudad
 */
public List<Persona> personasEnCiudad(String ciudad)

/**
 * Retorna una lista de las ciudades que contengan alguna persona que se 
 * llame como el nombre pasado como parámetro. La lista estará ordenada 
 * de mayor a menor, según el número de personas que cuenten con ese nombre.
 * 
 * Si ninguna ciudad tiene personas con ese nombre, se retornará una 
 * lista con todas las ciudades.
 * 
 * @param nombre el nombre de la persona para la búsqueda
 * @return lista de ciudades
 */
public List<String> masCiudadNombre(String nombre)
```

Referencia rápida de colecciones

List

| Type      | Method                      | Description                                                                      |
| --------- | --------------------------- | -------------------------------------------------------------------------------- |
| `boolean` | `add(E e)`                  | Appends the specified element to the end of this list (optional).                |
| `void`    | `add(int index, E element)` | Inserts the specified element at the specified position in this list (optional). |
| `boolean` | `contains(Object o)`        | Returns true if this list contains the specified element.                        |
| `E`       | `get(int index)`            | Returns the element at the specified position in this list.                      |
| `boolean` | `isEmpty()`                 | Returns true if this list contains no elements.                                  |
| `E`       | `remove(int index)`         | Removes the element at the specified position in this list (optional).           |
| `int`     | `size()`                    | Returns the number of elements in this list.                                     |



Map

| Type      | Method                    | Description                                                                   |
| --------- | ------------------------- | ----------------------------------------------------------------------------- |
| `boolean` | `containsKey(Object key)` | Returns true if this map contains a mapping for the specified key.            |
| `V`       | `get(Object key)`         | Returns the value mapped to the key, or null if none exists.                  |
| `Set<K>`  | `keySet()`                | Returns a Set view of the keys contained in this map.                         |
| `V`       | `put(K key, V value)`     | Associates the specified value with the specified key in this map (optional). |
| `V`       | `remove(Object key)`      | Removes the mapping for a key from this map if present (optional).            |
| `int`     | `size()`                  | Returns the number of key-value mappings in this map.                         |

Nota: Se pueden utilizar colecciones adicionales con otras estructuras de datos, como podría ser un `Set` en un `for` para recorrer las claves de un `Map`.

??? note "Mostrar solución"
    ```{.java .numberLines fontSize=/footnotesize}
    
    import java.util.ArrayList;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    import java.util.Set;
    
    public class GestorPersonas {
    
      Map<String, List<Persona>> mapCiudadPersona = new HashMap<String, List<Persona>>();
    
      public GestorPersonas(Persona[] arrayPersonas) {
        for(Persona persona : arrayPersonas) {
          if (mapCiudadPersona.get(persona.getCiudad()) == null) {
            List<Persona> personas = new ArrayList<Persona>();
            personas.add(persona);
            mapCiudadPersona.put(persona.getCiudad(), personas);
          } else {
            List<Persona> personas = mapCiudadPersona.get(persona.getCiudad());
            personas.add(persona);
          }
        }
      }
    
      public List<Persona> PersonasEnCiudad(String ciudad) {
        return mapCiudadPersona.get(ciudad);
      }
    
      public List <String> masCiudadNombre (String nombre) {
    
        int nMaxPersonas = 0;
        List<String> ciudadesMas = new ArrayList<String>();
        Set<String> ciudades = mapCiudadPersona.keySet();
    
        for(String ciudad : ciudades) {
          int nPersonas = 0;
          for(Persona persona : mapCiudadPersona.get(ciudad)) {
            if (persona.getNombre() == nombre) {
              nPersonas ++;
            }
          }
        
          if (nPersonas == nMaxPersonas) {
            ciudadesMas.add(ciudad);
          } 
          if (nPersonas > nMaxPersonas) {
            nMaxPersonas = nPersonas;
            ciudadesMas = new ArrayList<String>();
            ciudadesMas.add(ciudad);
          }
        }
        return ciudadesMas;
      }
    }
    ```
    
    La documentación de la función describe un proceso diferente.
    Una opción para resolverlo es esta:
    
    ```{.java .numberLines fontSize=/footnotesize}
    
    import java.util.ArrayList;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    import java.util.Set;
    
    public class GestorPersonas {
    
      Map<String, List<Persona>> mapCiudadPersona = new HashMap<String, List<Persona>>();
    
      public GestorPersonas(Persona[] arrayPersonas) {
        for(Persona persona : arrayPersonas) {
          if (mapCiudadPersona.get(persona.getCiudad()) == null) {
            List<Persona> personas = new ArrayList<Persona>();
            personas.add(persona);
            mapCiudadPersona.put(persona.getCiudad(), personas);
          } else {
            List<Persona> personas = mapCiudadPersona.get(persona.getCiudad());
            personas.add(persona);
          }
        }
      }
    
      public List<Persona> PersonasEnCiudad(String ciudad) {
        return mapCiudadPersona.get(ciudad);
      }
    
      public List <String> masCiudadNombre (String nombre) {
        int nMaxPersonas = 0;
        List<String> ciudades = new ArrayList<String>();
        List<Integer> contadores = new ArrayList<Integer>();
    
        for(String ciudad: mapCiudadPersona.keySet()) {
          int nPersonas = 0;
          for(Persona persona : mapCiudadPersona.get(ciudad)) {
            if (persona.getNombre() == nombre) {
              nPersonas++;
            }
          }
          int pos = ciudades.size();
          while(pos > 0 && contadores.get(pos-1) < nPersonas) {
              pos--;
          }
          ciudades.add(pos, ciudad);
          contadores.add(pos, nPersonas);
        }
        if(ciudades.isEmpty() {
            ciudades.addAll(mapCiudadPersona.keySet());
        }
        return ciudades;
      }
    }
    ```