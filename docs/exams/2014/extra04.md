---
id: ex-2014-04
year: 2014
exam: extraordinario
tags:
 - android
---

- (a) (0,8 puntos) Una aplicación Android llamada APP está ejecutándose y dispone del foco (interactúa con el usuario). Supongamos que se recibe una llamada telefónica, el usuario la atiende y luego cuelga. ¿Cuáles son los métodos del ciclo de vida de APP llamados?

??? note "Mostrar solución"
    La secuencia más común es:

    ```
    onPause()
    onStop()
    onRestart()
    onStart()
    onResume()
    ```

    pero también puede ocurrir la siguiente secuencia:

    ```
    onPause()
    onStop()
    onDestroy()
    onCreate()
    onStart()
    onResume()
    ```

    También podría ocurrir que la llamada entrante no llegue a retirar toda la actividad de la pantalla sino
    que quede en el fondo. En ese caso la secuencia sería:

    ```
    onPause()
    onResume()
    ```

    Todas las soluciones anteriores se consideran válidas.


- (b) (0,7 puntos) Describir brevemente qué es y para qué se usa un `SimpleCursorAdapter`.

??? note "Mostrar solución"
    Es un mecanismo que sirve para conectar el cursor con el que se accede a las filas que resultan de una consulta en una base datos con una `ListView` definida en el layout de una actividad. Se usa para mostrar los resultados de una consulta en una pantalla

- (c) (1 punto) En la actividad principal de una aplicación hay un botón que tiene asociado un método `onClick` que lanza la ejecución de una tarea asíncrona para cargar un fichero remoto. Indicar qué métodos hay que programar en la clase que implementa la `AsyncTask`, en qué hebra (thread) se ejecuta cada uno de ellos, y describa sucintamente qué hacen.

??? note "Mostrar solución"
    Suponiendo que la cabecera de la clase es:

    ```java
    class MyClass extends AsyncTask<Params, Progress, Result>
    ```
    
    los métodos que hay que programar son:
    
    ```java
    void onPreExecute()
    ```
    
    Se ejecuta en la `UIThread`, cuando se llama a `execute()`. Sirve para iniciar la tarea antes de empezar a ejecutar `doInbackground`.
    
    ```java
    Result doInBackground(Params…)
    ```
    
    Se ejecuta en la hebra auxiliar. Es equivalente a `run()` en las threads normales. `Params` son los parámetros que se le pasan al arrancar la tarea.
    
    ```java
    void onProgressUpdate (Progress…)
    ```
    
    Se ejecuta en la `UIThread` cada vez que se llama a `publishProgress(Progress…)` desde el cuerpo de `doInBackground`.
    
    ```java
    void onPostExecute (Result)
    ```
    
    Se ejecuta en la `UIThread` cuando termina `doInBackground` (con `return Result`).
    
    