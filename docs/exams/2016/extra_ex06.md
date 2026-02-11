---
id: ex-2016-06
year: 2016
exam: extraordinario
tags:
 - ???
---

Se quiere construir un diccionario donde las claves son `Object` que no se pueden comparar entre sí. Los valores también son `Object` de Java. Para ello se ha decidido programar un árbol binario de búsqueda, usando el hash de la clave como criterio para optar por el subárbol izquierdo o el derecho.

Se pide programar una clase `BST_Object` que incorpore el método
```java
void put(Object clave, Object valor)
```
que inserta un valor asociado a la clave; si la clave ya existía, se reemplaza el antiguo valor por el nuevo 

- (a) (1 punto) Programe los campos, el constructor y el método `put()`. No es necesario que programe más métodos.

??? note "Mostrar solución"
    ```java
    public class BST_Object {
    
        private Nodo root = null;
    
        public void put(Object clave, Object valor) {
            if (clave == null)
                throw new IllegalArgumentException("put(null, valor)");
            root = put(root, clave, valor);
        }
    
        private Nodo put(Nodo nodo, Object clave, Object valor) {
            if (nodo == null)
                return new Nodo(clave, valor);
    
            if (clave.equals(nodo.clave))
                nodo.valor = valor;
            else if (clave.hashCode() <= nodo.clave.hashCode())
                nodo.izq = put(nodo.izq, clave, valor);
            else
                nodo.der = put(nodo.der, clave, valor);
    
            return nodo;
        }
    
        private class Nodo {
            Object clave;
            Object valor;
            Nodo izq;
            Nodo der;
    
            Nodo(Object clave, Object valor) {
                this.clave = clave;
                this.valor = valor;
            }
        }
    }
    ```