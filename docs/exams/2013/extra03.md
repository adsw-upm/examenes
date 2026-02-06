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
01 public class MainActivity extends Activity {
02 
03     public static final int LANZA_A = 0;
04     public static final int LANZA_B = 1;
05
06     @Override
07     protected void onCreate(Bundle savedInstanceState) {
08         super.onCreate(savedInstanceState);
09         setContentView(R.layout.activity_main);
10
11         String[] acciones = {"lanzar", "terminar"};
12         setListAdapter(new ArrayAdapter<String>(
13                 this,
14                 android.R.layout.simple_list_item_1,
15                 acciones));
16     }
17
18     private void lanza() {
19         Intent lanzaA = new Intent(this, ActivityA.class);
20         if (startActivityForResult(lanzaA, LANZA_A) == RESULT_OK) {
21             Intent lanzaB = new Intent(this, ActivityB.class);
22             startActivityForResult(lanzaB, LANZA_B);
23         }
24     }
25
26     @Override
27     public void onListItemClick(ListView l, View v, int position, long id) {
28         super.onListItemClick(l, v, position, id);
29         switch (position) {
30             case 0: {
31                 lanza();
32                 break;
33             }
34             case 1: {
35                 finish();
36                 break;
37             }
38             default: { }
39         }
40     }
41
42     public static void main(String[] args) {
43         onCreate(this);
44     }
45 }
```

??? note "Mostrar solución"
    La línea 01 se reescribe para que quede como sigue:
    ```java
    public class MainActivity extends ListActivity {
    ```

    Después de la línea 19 se añade:
    ```java
    startActivityForResult(lanzaA, LANZA_A);
    ```
    
    Las líneas 20 a 23 se borran.

    Después de la línea 24 se añade:
    ```java
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == LANZA_A) {
                if (resultCode == RESULT_OK) {
                        Intent lanzaB = new Intent(this, ActivityB.class);
                        startActivity(lanzaB);
                }
        }
    }
    ```

    Las líneas  y 42 a  44 se borran.