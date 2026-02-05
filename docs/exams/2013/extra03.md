---
id: ex-2013-03
year: 2013
exam: extraordinario
tags:
    - android
---

- (a) (4 puntos) Se desea programar una aplicación compuesta por tres actividades: ```MainActivity``` (actividad inicial), ```ActivityA```, y ```ActivityB```. La tarea de ```MainActivity``` consiste en mostrar una lista con dos opciones al usuario: *lanzar* y *terminar*.

Si el usuario pulsa *lanzar*, se lanza la actividad `ActivityA`, que devuelve como resultado un código que indica si la actividad ha terminado con éxito o no (`RESULT_OK` o `RESULT_CANCELED`). Si el resultado es `RESULT_OK`, se lanza la actividad `ActivityB`, sin esperar a que devuelva ningún resultado.

Mire la solución que se proporciona a continuación e indique si es correcta o no. En caso de tener fallos, indique qué fallos hay y cómo se corrigen.

```java
public class MainActivity extends Activity {

    public static final int LANZA_A = 0;
    public static final int LANZA_B = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        String[] acciones = {"lanzar", "terminar"};
        setListAdapter(new ArrayAdapter<String>(
                this,
                android.R.layout.simple_list_item_1,
                acciones));
    }

    private void lanza() {
        Intent lanzaA = new Intent(this, ActivityA.class);
        if (startActivityForResult(lanzaA, LANZA_A) == RESULT_OK) {
            Intent lanzaB = new Intent(this, ActivityB.class);
            startActivityForResult(lanzaB, LANZA_B);
        }
    }

    @Override
    public void onListItemClick(ListView l, View v, int position, long id) {
        super.onListItemClick(l, v, position, id);
        switch (position) {
            case 0: {
                lanza();
                break;
            }
            case 1: {
                finish();
                break;
            }
            default: { }
        }
    }

    public static void main(String[] args) {
        onCreate(this);
    }
}
```

??? note "Mostrar solución"
    Se indican los cambios sobre el código original

    ```java
    public class MainActivity extends Activity ListActivity {
    ```
    ```java
    ~~public class MainActivity extends Activity ListActivity {~~
    ```
    ```java
        public static final int LANZA_A = 0;
        public static final int LANZA_B = 1;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
            String[] acciones = {"lanzar", "terminar"};
            setListAdapter(new ArrayAdapter<String>(
                    this,
                    android.R.layout.simple_list_item_1,
                    acciones));
        }

        private void lanza() {
            Intent lanzaA = new Intent(this, ActivityA.class);
            startActivityForResult(lanzaA, LANZA_A);
    ```
    ```java
            ~~if (startActivityForResult(lanzaA, LANZA_A) == RESULT_OK) {~~
                ~~Intent lanzaB = new Intent(this, ActivityB.class);~~
                ~~startActivityForResult(lanzaB, LANZA_B);~~
            ~~}~~
    ```
    ```java
        }

        protected void onActivityResult(int requestCode, int resultCode, Intent data) {
            if (requestCode == LANZA_A) {
                if (resultCode == RESULT_OK) {
                    Intent lanzaB = new Intent(this, ActivityB.class);
                    startActivity(lanzaB);
                }
            }
        }

        @Override
        public void onListItemClick(ListView l, View v, int position, long id) {
            super.onListItemClick(l, v, position, id);
            switch (position) {
                case 0: {lanza(); break;}
                case 1: {finish(); break;}
                default: { }
                }
            }
    ```
    ```java
            ~~public static void main(String[] args) {~~    // Las actividades en Android siguen un ciclo de vida,
                ~~onCreate(this);~~                         // no tienen main
            ~~}~~
        }
    ```