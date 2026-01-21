---
id: ex-2018-06
year: 2018
exam: extraordinario
tags:
 - android
---

Para la aplicación Android DaysUntil se desea añadir la posibilidad de añadir una descripción del evento introducido por el usuario. Esta información es opcional para la funcionalidad básica de la aplicación. Sin embargo, en caso de existir una descripción, esta debe incluirse en la información pasada como intención implícita para la creación de un evento en el calendario del usuario al pulsar un botón.

Siendo el esqueleto del código el siguiente:
```java
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    /** Devuelve el nombre del evento introducido por el usuario */
    private String getEvento () { ... }

    /** Devuelve la fecha del evento introducida por el usuario */
    private Calendar getFecha () { ... }

    /** 
     * A partir de un nombre y una fecha crea una intención implícita para la
     * inserción de un nuevo evento en un calendario
     */
    private Intent eventIntent (String nombre, Calendar fecha) { ... }

    public void crearEvento (View v) {
        // Completar
    }
}
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<android.support.constraint.ConstraintLayout
    … >

    <LinearLayout … >
        <EditText
            android:id="@+id/eventName"
            … />
        <EditText
            android:id="@+id/eventDate"
            … />
    </LinearLayout>

</android.support.constraint.ConstraintLayout>
```

- (a) Complete el código asociado a dicha funcionalidad, tanto en el código java como en la definición del layout asociado a la actividad en cuestión. Considere implementados los métodos getNombre y getFecha. Ha de implementar completamente cualquier otro método auxiliar que considere necesario. Nota: la clave esperada por la intención de crear un evento para la descripción del mismo es ```java CalendarContract.Events.DESCRIPTION ```.

??? note "Mostrar solución"
    ```java
    public class MainActivity extends AppCompatActivity {

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
        }

        /** Devuelve el nombre del evento introducido por el usuario */
        private String getEvento() { ... }

        /** Devuelve la fecha del evento introducida por el usuario */
        private Calendar getFecha() { ... }

        /**
         * A partir de un nombre y una fecha crea una intención implícita para la inserción de un
         * nuevo evento en un calendario
         */
        private Intent eventIntent(String nombre, Calendar fecha) { ... }

        public void crearEvento(View v) {
            EditText eventDescription = eventDescription = (EditText)
                    findViewById(R.id.eventDescription);

            Intent intent = eventIntent(getEvento(), getFecha());

            if (eventDescription.getText().toString().length() > 0) {
                intent.putExtra(CalendarContract.Events.DESCRIPTION,
                        eventDescription.getText().toString());
            }

            startActivity(intent);
        }
    }
    ```

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <android.support.constraint.ConstraintLayout
        … >

        <LinearLayout … >
            <EditText
                android:id="@+id/eventName"
                … />

            <EditText
                android:id="@+id/eventDate"
                … />

            <EditText
                android:id="@+id/eventDescription"
                android:hint="Event description"
                … />

            <Button
                android:text="Add event to calendar"
                android:onClick="crearEvento"/>
        </LinearLayout>

    </android.support.constraint.ConstraintLayout>
    ```
