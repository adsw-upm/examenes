---
id: ex-2025-03
year: 2025
exam: extraordinario
tags:
 - complejidad
---

Tres hebras Java de dos tipos diferentes, tipos A y B, entran en una sala para intercambiar tokens. Las hebras de tipo A solo salen de la sala cuando han intercambiado tokens con las dos hebras de tipo B, y las hebras de tipo B intercambian un solo token, cada una, con la hebra de tipo A. Las tres hebras no salen de la sala mientras que todas no han intercambiado sus tokens, y cuando las tres han intercambiado deben salir de la sala y más adelante volver a entrar para iniciar nuevos intercambios. Las hebras solo empiezan a intercambiar tokens cuando están las tres en la sala.

- (a) (5 puntos) Desarrollar un monitor Java que represente la ejecución de las hebras en la sala. En esta implementación, para que una hebra B salga de la sala, la hebra A con la que intercambian token debe haber intercambiado con dos hebras de tipo B. Mientras las 3 hebras están realizando el intercambio, ninguna otra hebra puede entrar en la sala. El monitor Java de la sala debe implementar el siguiente interfaz Java:

```{.java .numberLines}
 public interface ISalaTokens {

	// Entrada en la sala de la hebra A. Entra con 2 tokens y el resultado es un array 
	// con los dos tokens que le dan las hebras B
	String[] entraA(String token1, String token2) throws InterruptedException;

	// Entrada en la sala de las hebras B con 1 token cada una y el resultado es el token
	// que le ha dado la hebra A
	String entraB(String token) throws InterruptedException;	
}
```

Podemos suponer que el código de las hebras es el siguiente:
```java
// Hebra de tipo A
private Set<String> colec=new HashSet<String>();
private ISalaTokens sala;
private String[] tokens = new String[2]; 
public void run() {
  while (true) {
    tokens=buscarTokensA();
    if (!colec.contains(tokens[0]) && 
        !colec.contains(tokens[1]))
      tokens=sala.entraA(tokens[0],tokens[1]);
    colec.add(tokens[0]); colec.add(tokens[1]);
  }
}

// Hebra de tipo B
private Set<String> colec=new HashSet<String>();
private ISalaTokens sala;
private String token=null;
public void run() {
  while (true) {
    token=buscarTokenB();
    if (!colec.contains(token))
      token=sala.entraB(token);
    colec.add(token);
  }
}
```

Nota: Suponga que los métodos `buscarTokensA` y `buscarTokenB` están implementados y devuelven los tokens necesarios para el intercambio.

??? note "Mostrar solución"
    ```{.java .numberLines}
    public class SalaTokens implements ISalaTokens {
        private boolean esperandoA= false;
        private int esperandoB = 0;
        private String[] tokensB=new String[2];
        private String[] tokensA=new String[2];
    
        private boolean aPreparado = false;
        private int numBesperaA = 0;
    
        public synchronized String[] entraA(String token1, String token2) throws InterruptedException {
            esperandoA=true;
            while (esperandoB < 2) {
                wait();
            }
    
            aPreparado = true;
            tokensA[0]=token1;
            tokensA[1]=token2;
            numBesperaA = 0;
            notifyAll();
    
            while (numBesperaA < 2) {
                wait();
            }
    
            String[] tokens=new String[2];
            tokens[0]=tokensB[0]; tokens[1]=tokensB[1];
    
            aPreparado = false;
            notifyAll();
            return tokens;
        }
    
        public synchronized String entraB(String token) throws InterruptedException {
            esperandoB++;
            notifyAll();
    
            while (!aPreparado) {
                wait();
            }
            
            int id;
            tokensB[id=numBesperaA++]=token;
            esperandoB--;
            notifyAll();
    
            while (aPreparado) {
                wait();
            }
            return tokensA[id];
        }
    }
    ```