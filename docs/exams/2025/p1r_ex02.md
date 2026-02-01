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

### Documentación de la clase GestorPersonas
```{=latex}
\begin{minipage}[thp]{13cm}
```
```{.java fontSize=/footnotesize}
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

```{=latex}

\end{minipage}
\begin{minipage}[thp]{5cm}
\begin{center}

```
![](img/gestorpersonas.png){width=5cm}

```{=latex}
\end{center}
\end{minipage}

\vspace{-0.2cm}
```

### Referencia rápida de colecciones
```{=latex}

\vspace{-0.2cm}
\begin{table}[h!]
  \centering
  \begin{footnotesize}

  \begin{minipage}{.48\linewidth}
    \centering
    \textbf{List}\\[6pt]
    \begin{tabular}{|l|p{6.5cm}|}
      \hline
      \textbf{Type} & \textbf{Method and Description} \\
      \hline
      boolean & \texttt{add(E e)} – Appends the specified element to the end of this list (optional). \\
      \hline
      void & \texttt{add(int index, E element)} – Inserts the specified element at the specified position in this list (optional). \\
      \hline
      boolean & \texttt{contains(Object o)} – Returns \texttt{true} if this list contains the specified element. \\
      \hline
      \texttt{E} & \texttt{get(int index)} – Returns the element at the specified position in this list. \\
      \hline
      boolean & \texttt{isEmpty()} – Returns \texttt{true} if this list contains no elements. \\
      \hline
      \texttt{E} & \texttt{remove(int index)} – Removes the element at the specified position in this list (optional). \\
      \hline
      int & \texttt{size()} – Returns the number of elements in this list. \\
      \hline
    \end{tabular}
  \end{minipage}
  \hfill
  \begin{minipage}{.48\linewidth}
    \centering
    \textbf{Map}\\[6pt]
    \begin{tabular}{|l|p{6.5cm}|}
      \hline
      \textbf{Type} & \textbf{Method and Description} \\
      \hline
      boolean & \texttt{containsKey(Object key)} – Returns \texttt{true} if this map contains a mapping for the specified key. \\
      \hline
      \texttt{V} & \texttt{get(Object key)} – Returns the value mapped to the key, or \texttt{null} if none exists. \\
      \hline
      \texttt{Set<K>} & \texttt{keySet()} – Returns a \texttt{Set} view of the keys contained in this map. \\
      \hline
      \texttt{V} & \texttt{put(K key, V value)} – Associates the specified value with the specified key in this map (optional). \\
      \hline
      \texttt{V} & \texttt{remove(Object key)} – Removes the mapping for a key from this map if present (optional). \\
      \hline
      int & \texttt{size()} – Returns the number of key-value mappings in this map. \\
      \hline
    \end{tabular}
  \end{minipage}
  \end{footnotesize}
\end{table}
```

**Nota:** Se pueden utilizar colecciones adicionales con otras estructuras de datos, como podría ser un `Set` en un `for` para recorrer las claves de un `Map`.

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