---
id: ex-2014-03
year: 2014
exam: extraordinario
tags:
 - android
---

Sobre el proyecto del pacman, deseamos mover funcionalidad del menú a botones:

![](./extra/extra_03.png)

Se pide, siendo la respuesta razonada, incluyendo código java y especificaciones en XML, aunque no sea necesario que la sintaxis de java y xml sea perfectamente correcta:

- (a) (1 punto) ¿Qué cambios hay que hacer para poner botones? Indique ficheros java y ficheros de recursos que hay que modificar y en qué consiste la modificación.

??? note "Mostrar solución"
    Hay que añadir una fila de botones en `res/layout/main.xml`

    ```xml
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center" >

        <Button
            android:id="@+id/boton_reset"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:onClick="clic"
            android:text="RESET" />

        <Button
            android:id="@+id/boton_fantasma"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:onClick="clic"
            android:text="fantasma" />

        <Button
            android:id="@+id/boton_depredador"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:onClick="clic"
            android:text="depredador" />
    </LinearLayout>
    ```

    Hay que asociar la funcionalidad a cada botón en `MainActivity.java`

    ```java
    public void clic(View view) {
        Escenario escenario = Escenario.getInstance();
        switch(view.getId()) {
            case R.id.boton_reset:
                escenario.restart();
                return;
            case R.id.boton_fantasma:
                escenario.addMovil(this, R.id.fantasma00);
                return;
            case R.id.boton_depredador:
                escenario.addMovil(this, R.id.depredador);
                return;
        }
    }
    ```

    Si se van a eliminar las entradas del menú, hay que revisar los `R.id` que desaparecen, ajustando los identificadores que se usan en cada parte del código.

    NOTA: Hay otras formas de hacerlo:

    - En el layout: identificando cada botón por un `onClick()` específico.

    - En java, en `onCreate()`: localizando los botones y asociándoles la funcionalidad. Por ejemplo:

    ```java
    Button bv = (Button) findViewById(R.id.boton_reset);
    bv.setOnClickListener(new OnClickListener() {
        @Override
        public void onClick(View v) {
            Escenario escenario = Escenario.getInstance();
            escenario.restart();
        }
    });
    ```

    - En java, hacemos que la clase `MainActivity` implemente `OnClickListener` y escribimos el método `onClick()` en la clase principal y la asociamos a cada botón:

    ```java
    public class MainActivity extends … implements OnClickListener {

        // en onCreate():
        Button botonReset = (Button)rootView.findViewById(R.id.boton_reset);
        botonReset.setOnClickListener(this);

        // en la clase MainActivity:
        public void onClick(View view) {
            Escenario escenario = Escenario.getInstance();
            switch (view.getId()) {
                case R.id.boton_reset:
                    escenario.restart();
                    return;
                case R.id.boton_fantasma:
                    escenario.addMovil(this, R.id.fantasma00);
                    return;
                case R.id.boton_depredador:
                    escenario.addMovil(this, R.id.depredador);
                    return;
            }
        }
    }
    ```

- (b) (1 punto) ¿Qué cambios hay que hacer para eliminar entradas del menú? Indique ficheros java y ficheros de recursos que hay que modificar y en qué consiste la modificación.

??? note "Mostrar solución"
    Hay que eliminar las entradas de `res/menu/main.xml` que se muestran a continuación:

    ```xml
    <item
        android:id="@+id/button_reset"
        android:icon="@drawable/fantasma_rojo"
        android:showAsAction="ifRoom"
        android:title="@string/button_reset"/>

    <item
        android:id="@+id/fantasma00"
        android:icon="@drawable/fantasma_rojo"
        android:showAsAction="ifRoom"
        android:title="@string/fantasma00"/>

    <item
        android:id="@+id/depredador"
        android:icon="@drawable/anibal"
        android:showAsAction="ifRoom"
        android:title="@string/depredador"/>
    ```
    </del>

    Hay que eliminar la funcionalidad de la clase `MainActivity`:

    De:
    ```java
    01 @Override
    02 public boolean onOptionsItemSelected(MenuItem item) {
    03     Escenario escenario = Escenario.getInstance();
    04     switch (item.getItemId()) {
    05         case R.id.button_reset:
    06             escenario.restart();
    07             return true;
    08     }
    09     if (escenario.addMovil(this, item.getItemId()))
    10         return true;
    11     return super.onOptionsItemSelected(item);
    12 }
    ```
    Se eliminan las líneas 05 a 10.

    OJO: hemos eliminado la facilidad de añadir nuevos fantasmas sin más que añadirlos en la especificación xml del menú.


- (c) (0,5 puntos) ¿Podemos mantener ambos? Es decir, la misma funcionalidad accesible por menú y por botón.

??? note "Mostrar solución"
    Sí. Se pueden añadir los botones y dejar el código para el menú. La misma función se puede realizar de 2 formas: por botón y por menú.

