---
id: ex-2016-07
year: 2016
exam: extraordinario
tags:
 - android
---

En una aplicación Android, se dispone de la clase `RssRetrieveTask`, que descarga asíncronamente una serie de noticias de una fuente seleccionada, con la siguiente cabecera:
```java
private class RssRetrieveTask extends AsyncTask<String, Void, Void> { ... }
```
donde el primer parámetro es una lista de `Strings`, la primera de las cuales es el URL de la fuente RSS de noticias, y el resto son palabras de filtrado.

En el `layout` de la actividad principal se ha definido un botón con identificador "@+id/boton_leer", y se pretende que, al pulsar el botón, se active la tarea asíncrona `RssRetrieveTask`. 

- (a) (1 punto) Escriba el código adecuado que atienda a la pulsación del botón de forma que se active esta tarea.

??? note "Mostrar solución"
    En el método `onCreate` se añaden las siguientes líneas:
    ```java
    Button readButton = (Button) findViewById(R.id.read_button);
    readButton.setOnClickListener(new ReadOnClickListener() {
        @Override
        public void onClick(View v) {
            try {
                String words = wordsEdit.getText().toString();
                String[] urls = getResources().getStringArray(R.array.feeds_url);
                String url = urls[feedSpinner.getSelectedItemPosition()];
                Log.d(TAG, "Palabras " + words);
                Log.d(TAG, "URL " + url);
                RssRetrieveTask task = new RssRetrieveTask();
                task.execute(url, words);
            } catch (Exception e) {
                Log.e(TAG, "Error " + e.toString());
                Toast.makeText(getBaseContext(), "Error al recuperar las noticias",
                        Toast.LENGTH_LONG).show();
            }
        }
    });
    ```

    Notas: 

    * Se admiten las otras dos formas de asignar un método al `listener` de un `button`;
    * Nota 2: las sentencias `Log` y `Toast` son absolutamente opcionales y no influyen en la nota.