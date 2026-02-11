---
id: ex-2016-05
year: 2016
exam: extraordinario
tags:
 - android
---

Se pretende realizar una aplicación Android que gestione las notas obtenidas por cada estudiante. En la primera pantalla, se pide el 'login' y 'password' al estudiante, con los cuales se puede acceder a un servidor que contiene las notas. Cuando las notas se han descargado, se presenta una pantalla en la que se muestra un listado con cada asignatura disponible y su calificación.

- (a) (1,25 puntos) Escriba una especificación de `layout` adecuada para la actividad principal. Este `layout` debe permitir introducir una cadena de 'login', una de 'password', y debe disponer de un botón para proceder a la descarga de las notas.

Nota: Si lo desea, para evitar que se vea la 'password' puede usar 
```java 
android:inputType="textPassword".
```

??? note "mostrar solución" 
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical"
        tools:context="es.upm.dit.adsw.descarganotas.MainActivity">

        <LinearLayout
            android:orientation="horizontal"
            android:layout_width="match_parent"
            android:layout_height="wrap_content">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Login:" />

            <EditText
                android:id="@+id/editLogin"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_weight="1" />
        </LinearLayout>

        <LinearLayout
            android:orientation="horizontal"
            android:layout_width="match_parent"
            android:layout_height="wrap_content">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Password:" />

            <EditText
                android:id="@+id/editText2"
                android:layout_width="fill_parent"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:inputType="textPassword" />
        </LinearLayout>

        <Button
            android:id="@+id/descargar"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Descargar" />

    </LinearLayout>
    ```
Se dispone de la siguiente clase auxiliar, denominada `BajarNotasAsyncTask`, con la siguiente cabecera:
```java
private class BajarNotaAsyncTask extends AsyncTask<String, Void, Void> { ... }
```

(b) (1,25 puntos) Escriba el código adecuado para que al pulsar el botón de la actividad principal, comience la descarga de las notas. Nota: NO CODIFIQUE la clase `BajarNotasAsyncTask`.

??? note "Mostrar solución"
    ```java
    Button descargar = (Button) findViewById(R.id.descargar);
    descargar.setOnClickListener(new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            EditText loginET = (EditText) findViewById(R.id.editLogin);
            EditText passwordET = (EditText) findViewById(R.id.editPassword);

            String login = loginET.getText().toString();
            String password = passwordET.getText().toString();

            BajarNotasAsyncTask task = new BajarNotasAsyncTask();
            task.execute(login, password);
        }
    });
    ```

Se dispone de las siguientes clases para almacenar las notas de los alumnos (están incompletas):
```java
class Nota { // esta clase tiene la nota de una asignatura
    private String asignatura;
    private double nota;

    // constructor y getters al uso
}

class ListaNotasSingleton {
    private static final List<Nota> listaNotas = new ArrayList<>();

    private ListaNotasSingleton() {
        /* nadie lo toca */
    }

    public static void add(Nota nota) {
        listaNotas.add(nota);
    }

    public static List<Nota> getNotas() {
        return listaNotas;
    }
}
```

La ejecución de `BajarNotasAsyncTask` añade en el singleton `ListaNotasSingleton` las notas obtenidas hasta el momento por el alumno.

- (c) (1,25 puntos) Sobreescriba el método adecuado de la clase `BajarNotasAsyncTask` de forma que, una vez bajadas las notas, se arranque una actividad denominada `NotasListActivity`.

??? note "Mostrar solución"
    ```java
    @Override
    protected void onPostExecute(Void v) {
        super.onPostExecute(v);
        Intent intent = new Intent(MainActivity.this, NotasListActivity.class);
        startActivity(intent);
    }
    ```

La actividad `NotasListActivity` presenta un `layout` denominado “activity_notas_list.xml”, en el cual está definido un widget `ListView` con identificador “@+id/listaNotas”. Además, se dispone de un `layout` para cada fila, denominado “nota_item_row.xml” y una clase adaptadora de la lista de notas denominada `NotasArrayAdapter`.

- (d) (1,25 puntos) Programe el método `onCreate` de la clase `NotasListActivity`

??? note "Mostrar solución"
    ```java
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_notas_list);

        ListView listView = (ListView) findViewById(R.id.listaNotas);

        NotasArrayAdapter adapter =
                new NotasArrayAdapter(
                        this,
                        R.layout.nota_item_row,
                        ListaNotasSingleton.getEntries()
                );

        listView.setAdapter(adapter);
        listView.setOnItemClickListener(new OnItemClickListenerListViewItem());
    }
    ```
