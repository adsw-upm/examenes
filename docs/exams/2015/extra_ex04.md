---
id: ex-2015-04
year: 2015
exam: extraordinario
tags:
 - android
---

Se pretende realizar una aplicación Android que gestione los gastos de un usuario. Cada vez que se realiza un gasto, el usuario puede introducir la cantidad gastada (“Importe”, campo numérico real) y en qué se lo ha gastado (“Concepto”, de tipo texto). Estos registros se guardarán en una base de datos sqlite, con una única tabla. La aplicación mostrará los registros existentes mediante una ListActivity. 

La aplicación dispone de un menú con dos opciones, “Añadir” y “Acerca de”. La especificación del menú es la siguiente:

```xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">

    <item
        android:id="@+id/annadir"
        android:title="Añadir" />

    <item
        android:id="@+id/ayuda"
        android:title="Acerca de" />

</menu>
```

La sentencia SQL para crear la tabla en la base de datos es:

```SQL
CREATE TABLE gastos (_id INTEGER PRIMARY KEY AUTOINCREMENT, Concepto TEXT NOT NULL, Importe REAL NOT NULL)
```

La aplicación dispone de un adaptador de bases de datos, con la siguiente codificación (parcial):


```java
public class DatabaseHelper {
    private SQLiteDatabase database;
    private MySQLiteHelper dbHelper;
    private static final int DATABASE_VERSION = 1;
    private static final String DATABASE_NAME = "libros.db";
    …
}
```

- (a) (1 punto) Escriba una sentencia SQL que devuelva todos los registros de la base de datos cuyo importe supere el valor de 50,00.

??? note "Mostrar solución"
    ```SQL
    SELECT * FROM gastos WHERE Importe > 50;
    ```


- (b) (1 punto) Sobreescriba el método adecuado de ListActivity para implementar el siguiente comportamiento:

    - 1) la opción “Acerca de” muestra un Toast con el nombre del autor del código (usted);
    - 2) la opción “Añadir” se lance otra actividad llamada “AnadirGastoActivity” que ya está implementada.

    Tenga en cuenta que “AnadirGastoActivity” devolverá un Intent con los datos del usuario.

??? note "Mostrar solución"
    ```java
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {

            case R.id.ayuda:
                Toast.makeText(
                        this,
                        getString(R.string.msg_ayuda),
                        Toast.LENGTH_SHORT
                ).show();
                return true;

            case R.id.annadir: {
                Intent miIntent = new Intent(
                        this,
                        AnadirGastoActivity.class
                );
                miIntent.putExtra(REQUEST_CODE, CREA_PRODUCTO);
                startActivityForResult(miIntent, CREA_PRODUCTO);
                return true;
            }

            default:
                return false;
        }
    }
    ```

- (c) (1 punto) ¿Qué métodos relativos al ciclo de vida de las actividades ListActivity y AnadirGastoActivity se ejecutan desde que se selecciona la opción “Añadir” del menú hasta que se vuelve a mostrar la lista de gasto? Escriba sólo el nombre del método y la actividad a la que pertenece, y el orden adecuado.

??? note "Mostrar solución"
    | Método      | Actividad           |
    | ----------- | ------------------- |
    | onPause()   | ListActivity        |
    | onCreate()  | AnadirGastoActivity |
    | onStart()   | AnadirGastoActivity |
    | onResume()  | AnadirGastoActivity |
    | onStop()    | AnadirGastoActivity |
    | onPause()   | AnadirGastoActivity |
    | onRestart() | ListActivity        |
    | onStart()   | ListActivity        |
    | onResume()  | ListActivity        |
    | onStop()    | AnadirGastoActivity |


- (d) (1 punto) Escriba un método de la clase DatabaseHelper que añada un nuevo registro a la base de datos. La información del Concepto y del Importe se pasará como parámetros del método.

??? note "Mostrar solución"
    ```java
    public long creaProducto(String gasto, float importe) {
        ContentValues valoresIniciales = new ContentValues();

        valoresIniciales.put("Concepto", gasto);
        valoresIniciales.put("Importe", importe);

        return db.insert(DATABASE_TABLE, null, valoresIniciales);
    }
    ```


- (e) (1 punto) Escriba una especificación de layout adecuada que se pueda utilizar en la actividad “AnadirGastoActivity”. Además de los campos de información, dispondrá de un botón “Guardar” y otro “Cancelar” (sólo hay que poner los botones). 

??? note "Mostrar solución"
    ```XML
    <?xml version="1.0" encoding="utf-8"?>
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:layout_width="fill_parent"
        android:layout_height="fill_parent "
        android:orientation="vertical">

        <LinearLayout
            android:layout_width="fill_parent"
            android:layout_height="wrap_content ">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Concepto " />

            <EditText
                android:id="@+id/editConcepto"
                android:layout_width="fill_parent"
                android:layout_height="wrap_content">
            </EditText>
        </LinearLayout>

        <LinearLayout
            android:layout_width="wrap_content"
            android:layout_height="wrap_content">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Cantidad “ />

            <EditText
                android:id="@+id/editTextCantidad"
                android:layout_width="fill_parent"
                android:layout_height="wrap_content"
                android:inputType="numberDecimal" />
        </LinearLayout>

        <LinearLayout android:orientation="horizontal">

            <Button
                android:id="@+id/buttonGuardar"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Guardar" />

            <Button
                android:id="@+id/buttonCancelar"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Cancelar" />
        </LinearLayout>

    </LinearLayout>
    ```
