
Instalar [JDK 21](https://www.oracle.com/pe/java/technologies/downloads/#jdk21-windows)

Instalar [IntelliJ IDEA edition](https://www.jetbrains.com/es-es/idea/download/?section=windows)

Instalar [Apache Netbeans](https://netbeans.apache.org/front/main/index.html)// no es de pago
##### Cambiar de tema a oscuro en Apache Netbeans
- [Descargar tema](https://draculatheme.com/netbeans)
- configurar en Tools->options->fonts y colors
    - importar el tema zip
- configurar en Tools->options->apariencia, pestaña Look and Feel, cambiar combo a FlatLaf Dark y marcar Maximize use of native look and feel
- En Tools->options->fonts & colors cambiar el combo profile a Dracula
- Importar nuevamente el tema
- En el proyecto click derecho, properties, build->compile, marcar Compile on Save

- Cuando se crea un proyecto simple: se selecciona la categoria Java with Ant
- Las variables se guardan en la RAM
    - Memoria Stack (Pila): Almacena variables primitivas
    - Memoria Heap: Almacena los objetos
JDK: Para crear las aplicaciones
    JRE:(pertenece al JDK) se usa para ejecutar
        JVM: Ejecuta el bytecode de jaba (independiente del OS)
            Intérprete JIT
            Recolector de basura (garbage)
#### Atajos
    presionar luego tabulador:
    psvm: crea el public static void main
    sout: system.out.println()
    soutv: para imprimir el nombre de la variable y su valor

#### Buenas prácticas
    Notación CamelCase:
        nombreCliente
        _nombre
        $apellidoCompleto

```java
System.out.println();//imprime salto de línea
```
#### variable VAR
    - se usa para definir los tipos implicitamente y el código sea mas legible
    - debe ser iniciada al declararse : var numero=10;
    - no puede ser inicializada con null: var numero =null;
    - una vez q se inicializa ya no se puede modificar su tipo de valor
    - S
```java
    var nombre = "Antonio";//el nombre es de tipo String para siempre
    long tipoLong = 987654321098765432L; // L o l para indicar tipo long
    float tipoFloat = 3.14F; // F o f para indicar tipo float
    System.out.println("tipoFloat = " + tipoFloat);
    double tipoDouble = 3.1315D; // D o d para indicar tipo double (opcional)
    System.out.println("tipoDouble = " + tipoDouble);
    System.out.println() // imprime un salto de linea
    System.out.print()// imprime en la misma linea

    var cadena4 = """
                Este es un texto
                multilinea
                mas 
                lineas
                """;
    System.out.println("cadena4 = " + cadena4);
```
#### constantes
    con la palabra final
```JAVA
    final var DIAS_SEMANA=7;
```

#### Métodos de cadena
```JAVA
var longitud = cadena1.length();
var nuevaCadena = cadena1.replace('o','a');
var mayusculas = cadena1.toUpperCase();
var minúsculas = cadena1.toLowerCase();
cadena2.trim();// Eliminar espacios
cadena2.strip();// Eliminar espacios al inicio y final
cadena1 == cadena3 // comparación por referencia
cadena1.equals(cadena3) // comparación por valor
cadena1.substring(0, 4)
cadena1.substring(4)// extrae desde el indice 4 en adelante
var a=5, b=3, c=7; // var no funciona para una declaracion compuesta de variables
int nroinicial;// cuando no se asigna valor, entonces es cero
var indice1 = cadena1.indexOf("Hola");
var indice2 = cadena1.lastIndexOf("Mundo");// devuelve el indice de la ultima aparicion de la subcadena
var indice3 = cadena1.lastIndexOf("Java");//subcadena no encontrada devuelve -1
var nuevaCadena = cadena.replace("Mundo", "a todos")
String resultado = cadena1 + cadena2;
var mensaje = saludo.concat(", ").concat(nombre).concat("!");
// Clase StringBuilder
// es más eficiente para concatenaciones repetitivas y en bucles, ya que es mutable y no crea nuevas instancias de cadena.
var sb = new StringBuilder();
sb.append(cadena1);
sb.append(cadena2);
var resultado = sb.toString();

// Clase StringBuffer: un poco mas lento q StringBuilder
// es similar a StringBuilder, pero es seguro para hilos (thread-safe), lo que lo hace adecuado para entornos multihilo.
var sb = new StringBuffer();
sb.append(cadena1);
sb.append(cadena2);
var resultado = sb.toString();
//Método String.join()
var mensaje = String.join(", ", saludo, nombre,...) + "!";

var dato = Integer.parseInt(new Scanner(System.in).nextLine());
// Verificar si el dato esta dentro de rango
var estaDentroRango = dato >= MINIMO && dato <= MAXIMO;
```

#### caracteres especiales

```java
    // '\n' - imprimir un salto de linea
    var cadena1 = "Hola\nMundo";
    // '\t' - tabulador
    var cadena2 = "\tHola\tMundo";
    // '\'' - agrega una comilla simple
    var cadena3 = "Hola \' Mundo";
    // '\"' - agrega una comilla doble
    var cadena4 = "Hola \" Mundo";
    // '\\' - caracter de diagonal invertida
    var cadena5 = "Hola \\ Mundo";
```

```java
import java.util.Scanner;
var consola = new Scanner(System.in); // in - input - entrada de datos
System.out.print("Escribe tu nombre: ");
var nombre = consola.nextLine();
System.out.println("nombre = " + nombre);

```
#### Conversion de datos
```java
        System.out.print("Proporciona un valor entero: ");
//      var enteroString = consola.nextLine();
//      var entero = Integer.parseInt(enteroString);
        var entero = Integer.parseInt(consola.nextLine());
        System.out.println("entero = " + entero);
        // Tipo flotante
        System.out.print("Proporciona un valor flotante: ");
        var flotante = Float.parseFloat(consola.nextLine());
        System.out.println("flotante = " + flotante);
        //Double.parseDouble()
        //Boolean.parseBoolean()
        var salarioEmpleado = Double.parseDouble(consola.nextLine());
        var esJefeDepartamento = Boolean.parseBoolean(consola.nextLine());
```

#### Formateo de cadenas
Resumen de Especificadores de Formato
• %s: Cadena de texto.
• %d: Entero decimal.
• %f: Número de punto flotante.
• %n: Nueva línea independiente de la plataforma.
• %t: Fecha y hora (requiere especificadores adicionales para el formato específico).

```java
    System.out.println("\tSalario: $%.2f".formatted(salarioEmpleado));
    System.out.printf("\tSalario: $%.2f%n", salarioEmpleado);// %n es salto de línea

    // String.format permite crear una nueva cadena con formato especificado.
    var mensaje = String.format("Nombre: %s, Edad: %d, Salario: %.2f", nombre, edad, salario);
    // System.out.printf permite formatear la salida directamente en la consola.
    System.out.printf("Nombre: %s, Edad: %d, Salario: %.2f%n", nombre, edad, salario);
    // Uso de Bloques de Texto (Text Blocks)
    // Los bloques de texto se introdujeron en Java 13 como una vista previa y se estabilizaron en
    // Java 15. Permiten escribir cadenas de texto multilínea de manera más fácil y legible.
    mensaje = """
        Nombre: %s
        Edad: %d
        Salario: %.2f
        """.formatted(nombre, edad, salario);
    System.out.println(mensaje);
    // %n imprime un salto de linea
    // \s Espacio en blanco
    // \t Tabulador
    var mensaje = """
            %nInformación del Empleado:\s
            -------------------------
            Nombre: %s
            Edad: %d
            Salario: %.2f
            -------------------------
    """.formatted(nombre, edad, salario);
    System.out.println(mensaje);
// el doble %% imprime solo %
    System.out.printf("""
            %nTicket de Venta
            ---------------
            Subtotal: $%.2f
            Impuesto (16%%): $%.2f
            Costo total de la compra: $%.2f
            """, subtotal, impuesto, costoTotalCompra);

    //Asegurar 4 dígitos para el número entero
    var numeroFormateado = String.format("%04d", numero);
    //Asegurar 2 dígitos decimales para el número de punto flotante
    var valorFormateado = String.format("%.2f", valor);
    //Asegurar 4 dígitos para el número entero
    System.out.printf("Número formateado (4 dígitos): %04d%n", numero);
    // Asegurar 2 dígitos decimales para el número de punto flotante
    System.out.printf("Valor formateado (2 dígitos decimales): %.2f%n", valor);
    // Formateo con text block
    var mensaje = """
            Número formateado (4 dígitos): %04d
            Valor formateado (2 dígitos decimales): %.2f
    """.formatted(numero, valor);
    System.out.println(mensaje);

    System.out.print("Ingresa el destino del paquete (nacional/internacional): ");
    String destino = consola.nextLine().strip().toLowerCase();

```

#### Aleatorios
```java
        // Generar un numero aleatorio entre 0 y 9
        var numeroAleatorio = random.nextInt(10);
        // Generar un numero aleatorio entre 1 y 10
        numeroAleatorio = random.nextInt(10) + 1;
        // Generar un numero flotante entre 0.0 y 1.0
        var flotanteAleatorio = random.nextFloat();
        // Simular el lanzamiento de un dado (1 y 6)
        var dado = random.nextInt(6) + 1;
```
#### Operadores unarios
```java
System.out.println("*** Operadores Unarios ***");
        int a = 3, b = -2, resultado;
        var c = true;
        // Operdor unario +
        resultado = +a;
        System.out.println("resultado +a = " + resultado);
        // Operador unario -
        resultado = -a;
        System.out.println("resultado -a = " + resultado);

        // Operadores unarios incremento/decremento
        //Pre-incremento
        a = 3;
        resultado = ++a; // primero se incrementa el valor
        System.out.println("resultado ++a = " + resultado);
        System.out.println("a ya se incremento = " + a);
        // Post-incremento
        a = 3;
        resultado = a++;//primero se usa el valor y despues se incrementa
        System.out.println("resultado a++ = " + resultado);
        System.out.println("a en este momento se incrementa = " + a);

        //Pre-decremento
        b = -2;
        resultado = --b;//primero se incrementa y despues se usa el valor
        System.out.println("resultado --b = " + resultado);
        System.out.println("b ya se decremento = " + b);
        //Post-decremento
        b = -2;
        resultado = b--;//primero se usa el valor, y despues se incrementa
        System.out.println("resultado b-- = " + resultado);
        System.out.println("b en este momento se decrementa = " + b);

        var precioLechuga = Double.parseDouble(consola.nextLine());
```

# Operador ternario
```JAVA
    var resultado = (numero % 2 == 0) ? "Par" : "Impar";
    var calificacion =  (nota >= 90) ? "A" :
                        (nota >= 80) ? "B" :
                        (nota >= 70) ? "C" :
                        (nota >= 60) ? "D" : "F";
    String estado = esActivo ? "Activo" : "Inactivo";  
    var resultado = (numero > 0) ? "Positivo" : (numero < 0) ? "Negativo" : "Cero";
                  
```

# Switch
```JAVA
    switch (expresion) {
        case valor1:
            // Bloque de código para el caso valor1
            break;
        case valor2:
            // Bloque de código para el caso valor2
            break;
        default:
            // Bloque de código para el caso por defecto
            break;
    }
    //En Java 12 y versiones posteriores,
    nombreDia = switch (dia) {
        case 1 -> "Lunes";
        case 2 -> "Martes";
        case 3 -> "Miércoles";
        case 4 -> "Jueves";
        case 5 -> "Viernes";
        case 6 -> "Sábado";
        case 7 -> "Domingo";
        default -> "Día inválido";
    };
    switch (mes) {
        case 1, 2, 12 -> estacion = "Invierno";
        case 3, 4, 5 -> estacion = "Primavera";
        case 6, 7, 8 -> estacion = "Verano";
        case 9, 10, 11 -> estacion = "Otoño";
        default -> estacion = "Estación desconocida";
    }
    // con yield devuelve un valor
    // Cálculo del envío del paquete usando switch con yield
    Double costoEnvio = switch (destino) {
        case "nacional" -> peso * TARIFA_NACIONAL;
        case "internacional" -> peso * TARIFA_INTERNACIONAL;
        default -> {
            System.out.println("Destino no válido. Ingresa el valor de nacional o internacional");
            yield null;
        }
    };

    String nombreDia = switch (dia) {
        case 1 -> "Lunes";
        case 2 -> "Martes";
        case 3 -> "Miércoles";
        case 4 -> "Jueves";
        case 5 -> "Viernes";
        case 6 -> "Sábado";
        case 7 -> "Domingo";
        default -> {
            yield "Día inválido"; // Devolver un valor con yield
        }
    };// cuando se asigna a una variable debe terminar con ;
    
    var mensajeAutenticacion = switch (usuario){
        case USUARIO_VALIDO -> {
            if(PASSWORD_VALIDO.equals(password))
                yield "Bienvenido al Sistema!";
            else
                yield "Password incorrecto, favor de corregirlo!";
        }
        default -> {
            if(PASSWORD_VALIDO.equals(password))
                yield "Usuario incorrecto, favor de corregirlo!";
            else
                yield "Usuario y password incorrectos, favor de corregirlos!";
        }
    };
```


