---
id: ex-2021-01
year: 2021
exam: parcial 1 recuperacion
tags:
 - hebras
---

Se quiere desarrollar un programa que analice un documento de texto y calcule el n!mero de veces que aparece cada palabra (String). El resultado es una lista de ContadorPalabra, que es una clase que se muestra a continuación:

```java
public class ContadorPalabra {
    String nombre; // Nombre en el documento
    int contador; //Núm. de veces que aparece
    ...
    // Están disponibles los getters y setters
}
```

En una fase inicial del programa, se crean dos hebras que analizan una mitad del documento. El resultado de cada hebra es una lista (java.util.List<ContadorPalabra>), con el contador de cada palabra de la mitad correspondiente. Los elementos de cada lista est"n ordenados por el atributo nombre de cada ContadorPalabra.

En este ejercicio, se quiere desarrollar un m#todo para agregar las
dos listas generadas de cada mitad. Se pide:

- (a) (1,5 puntos) Desarrolle el m#todo Menor, que recibe dos listas ordenadas y retorna el ContadorPalabra con la menor palabra en cualquiera de las dos mitades. 

```java
public ContadorPalabra Menor (
    java.util.List<ContadorPalabra> ag1,
    java.util.List<ContadorPalabra> ag2) { . . . }
```

??? note "Mostrar solución"
    ```java
    public ContadorPalabra Menor(
            java.util.List<ContadorPalabra> ag1,
            java.util.List<ContadorPalabra> ag2) {

        ContadorPalabra p1 = ag1.get(0);
        ContadorPalabra p2 = ag2.get(0);

        if (ag1.size() == 0 || ag1 == null) 
            return ag2.get(0);

        if (ag2.size() == 0 || ag2 == null) 
            return ag1.get(0);

        if (p1.getNombre().compareTo(p2.getNombre()) <= 0)
            return ag1.get(0);

        return ag2.get(0);
    }
    ```


- (b) (3,5 puntos) Desarrolle el m#todo Agregar, que recibe dos listas y retorna una lista ordenada que agregue los objetos PalabraContador de los parámetros de entrada. En concreto, calcula el valor de cada palabra en cada mitad en el documento. Este m#todo puede usar Menor, pero no es obligatorio. 

```java
public java.util.List<ContadorPalabra> Agregar(
java.util.List<ContadorPalabra> ag1,
java.util.List<ContadorPalabra> ag2))
{ . . . }
```

y

Ejemplo: Los dos parámetros de entrada de Agregar o Menor podrían ser:
```java
Ag1 = { [“adiós”, 3], [“bueno”, 1], [“hola”, 2], [“malo”, 4] }
Ag2 = { [“adiós”, 4], [“bueno”, 7], [“malo”, 2] }
```

La salida del método agregar sería:
```java
agregar = { [“adiós”, 7], [“bueno”, 8], [“hola”, 2], [“malo”, 6] }
```

A continuación se muestran algunos m#todos relevantes de la colección List.

![](./p1r/p1r_ex01.png)

??? note "Mostrar solución"
    ```java
    public java.util.List<ContadorPalabra> Agregar() {
        ContadorPalabra min;
        java.util.List<ContadorPalabra> agregado =
            new java.util.ArrayList<ContadorPalabra>();
    
        while ((ag1.size() != 0) || (ag2.size() != 0)) {
            min = Menor(ag1, ag2);
            ContadorPalabra aux = null;
    
            if (ag1.size() > 0) {
                if (min.getNombre() == ag1.get(0).getNombre()) {
                    if (aux == null) {
                        aux = ag1.remove(0);
                    }
                }
            }
    
            if (ag2.size() > 0) {
                if (min.getNombre() == ag2.get(0).getNombre()) {
                    if (aux == null) {
                        aux = ag2.remove(0);
                    } else {
                        aux.setContador(
                            aux.getContador() + ag2.get(0).getContador()
                        );
                        ag2.remove(0);
                    }
                }
            }
    
            agregado.add(aux);
        }
        return agregado;
    }
    ```


