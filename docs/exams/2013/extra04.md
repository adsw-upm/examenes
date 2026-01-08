---
id: ex-2013-04
year: 2013
exam: extraordinario
tags:
    - android
---

Se desea modificar la aplicación `Teleconote` de manera que la pantalla con la lista de notas (controlada por la actividad `ListaNotasActivity`) se comporte de forma que, al pinchar en una nota, si está cifrada, se descifre sin pedir ninguna contraseña. Si la nota no está cifrada, se deja como está.

Obsérvese que no hay que mostrar el contenido de la nota, sólo descifrarla en caso necesario desde `ListaNotasActivity`.

Puede suponer que la clase que contiene la tarea asíncrona, que programó en `DetalleNotaActivity`, está refactorizada como una clase de paquete, de la siguiente forma:

```java
public class Cifrar extends AsyncTask<?,?,?> {
    protected void onPreExecute() {...}

    @Override
    protected ... doInBackground(...) {...}

    protected void onProgressUpdate(...) {...}

    protected void onPostExecute(...) {...}
}
```

La tarea recibe varias cadenas (el título y contenido de la nota, así como su id), comunica el número de caracteres cifrados o descifrados, y devuelve el objeto nota con los campos `titulo` y `contenido` descifrados.

- (a) (3 puntos) Indique qué signatura debería tener la clase `Cifrar`.
??? note "Mostrar solución"
    La signatura correcta de la clase `Cifrar` es:

    ```java
    Cifrar<String, Integer, Nota>
    ```

- (b) (7 puntos) Indique los cambios necesarios para que se ejecute la tarea de descifrado con esta modificación. Tenga en cuenta que los cambios deben almacenarse en la base de datos, y que debe actualizarse la pantalla de `ListaNotasActivity`.

NOTA: Limítese a hacer los cambios necesarios. No es necesario volver a escribir el código de `Cifrar` ni las partes de `ListaNotasActivity` que no haya que modificar.

??? note "Mostrar solución"
    A continuación se muestran únicamente los cambios necesarios para ejecutar la tarea de descifrado desde `ListaNotasActivity`. Los cambios relevantes se destacan conceptualmente. 
    ```java
    @Override
    public void onListItemClick(ListView l, View v, int position, long id) {
        super.onListItemClick(l, v, position, id);
        Cursor c = notasCursor;
        c.moveToPosition(position);
    
        Nota nota = getNota(c);
        if ((nota != null) && (nota.isCifrado())) {
            new Cifrar().execute(
                nota.getContenido(),
                nota.getTitulo(),
                nota.getCategoria(),
                id + ""
            );
        }
        startActivityForResult(intent, MODIFICA_NOTA);
    }
    ```
    
    ```java
    private class Cifrar extends AsyncTask<String, Integer, Nota> {
    
        private final String CLAVE = new String("miclave");
        private long id = -1;
    
        // Se puede acceder a la UI
        @Override
        protected void onPreExecute() {
        }
    
        // Método de descifrado (no se modifica)
        private String descifra(String texto, String clave) {
            // Código existente que almacena el texto
            // descifrado en un buffer
            ...
            publishProgress(i);
            return buffer.toString();
        }
    
        // Ejecución en segundo plano
        @Override
        protected Nota doInBackground(String... params) {
            Log.i(TAG, "doInBackground");
    
            String titulo = params[0];
            String contenido = params[1];
            String categoria = params[2];
    
            if ((titulo == null) || (contenido == null) || (categoria == null))
                return null;
    
            try {
                id = Long.parseLong(params[3]);
            } catch (NumberFormatException e) {
                return null;
            }
    
            String tituloDescifrado = descifra(titulo, CLAVE);
            String contenidoDescifrado = descifra(contenido, CLAVE);
    
            Nota miNota = new Nota(
                tituloDescifrado,
                contenidoDescifrado,
                categoria,
                false
            );
            return miNota;
        }
    
        // Actualizaciones de progreso en la UI
        @Override
        protected void onProgressUpdate(Integer... value) {
            super.onProgressUpdate(value);
            Log.i(TAG, "onProgressUpdate");
            texto.append("
    Ejecutándose..." + value[0]);
            // Mostrar progreso por pantalla
        }
    
        // Al finalizar, se actualiza la BBDD y la lista
        @Override
        protected void onPostExecute(Nota miNota) {
            Log.i(TAG, "onPostExecute, nota Cifrada");
            notaDbAdaptador.actualizaNota(id, miNota);
            cursorAdapter.notifyDataSetChanged();
            actualizaLista();
        }
    }
    ```
