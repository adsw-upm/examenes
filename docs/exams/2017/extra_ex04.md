---
id: ex-2017-01
year: 2017
exam: extraordinario
tags:
 - android
---

Se dispone de una aplicación Android para la consulta de notas por parte de los alumnos. La aplicación consta de dos pantallas, denominadas MainActivity y ResultActivity.

En la primera pantalla (MainActivity), el usuario introduce su identificación (nombre y apellidos) y el código numérico de la asignatura a consultar. Dispone de un botón con el texto “Consultar” que, al pulsarse, pasa a la segunda pantalla ResultActivity, mediante un Intent con la información de identificación del alumno y el código de la asignatura. La primera pantalla dispone de un layout en el que se dispone de dos EditText, uno para el nombre y otro para el código, mas el botón para realizar la consulta.

En la segunda pantalla (ResultActivity), se consultará la base de datos de notas y se presentará la nota obtenida.

Esta pantalla no es de nuestro interés.

- (a) (1 punto) Completar el código del método onCreate de la clase MainActivity.

??? note "Mostrar solución"
    ```java
    public class MainActivity extends AppCompatActivity {
        private EditText etIdentificacion;
        private EditText etCodigo;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);

            etIdentificacion = (EditText) findViewById(R.id.editIdentificador);
            etCodigo = (EditText) findViewById(R.id.editCodigo);

            Button b = (Button) findViewById(R.id.botonConsultar);
            b.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    // método a rellenar
                }
            });
        }
    }

    // Escriba a continuación el cuerpo del método onClick.
    public void onClick(View v) {
        String id = etIdentificacion.getText().toString();
        String codigo = etCodigo.getText().toString();
        Intent i = new Intent(getApplicationContext(), ResultActivity.class);
        i.putExtra("ID", id);
        i.putExtra("CODIGO", codigo);
        startActivity(i);
    }    
    ```


- (b) (1 punto) Indicar los métodos del ciclo de vida que se invocarán de la actividad MainActivity y ResultActivity en el orden correcto.

??? note "Mostrar solución"
    ```java
    MainActivity.onPause()
    ResultActivity,onCreate()
    ResultActivity.onStart()
    ResultActivity.onResume()
    MainActivity.onStop()

    // Se puede añadir MainActivity.onDestroy()
    ```

