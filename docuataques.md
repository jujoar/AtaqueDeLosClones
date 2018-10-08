# Instituto Tecnológico de Costa Rica y

# Universidad Nacional de Costa Rica

# Sede Interuniversitaria de Alajuela

## Proyecto Programado: El Ataque de los Clones

## Curso: Seguridad Informática

## Profesor:  Kevin Moraga

## Integrantes:

## Luis Alejandro Castaing

## Luis Carlos Sánchez

## Juan José Salas

## Esteban Soto

## 8 de Octubre del 2018


## 1.Introducción

En la actualidad, phishing es uno de los ataques más populares donde se
obtienen credenciales o información personal de la víctima. El presente trabajo tiene
como fin realizar un ataque de este tipo mediante la clonación de una página web
donde luego de que el usuario introduzca sus credenciales se deberá redireccionar
a la página real con el fin de que parezca que los datos fueron introducidos
erróneamente. Además se realizará una prueba de estrés que sería un ataque DoS.
Todo esto con el fin de que las personas comprendan cómo funciona y eviten ser
víctimas de un ataque de phishing diferenciando los diferentes detalles que se
logran apreciar como la URL del sitio web o el diseño del mismo.

## 2. Ambiente de desarrollo

Para el desarrollo de las diferentes tareas se usaron varias herramientas.

**- Clonación de la página y ataque de phishing:**
    Para poder hacer la clonación de la página, en este caso Facebook y para
    realizar el ataque de phishing se usaron varias herramientas como Sublime
    Text un editor de texto, donde se copió todo el código fuente con el fin de
    realizar la página idéntica a la real, además para poder programar la
    conexión a la base de datos, las consultas a este y otras funciones. Se hizo
    uso de Tor Browser con el fin de poder entrar al sitio web, introducir las
    credenciales y saber si estas se guardaban en la base de datos y todo
    funcionaba correctamente. Se utilizó PHP para programar junto con la base
    de datos MySQL gracias a phpMyAdmin y todos los servicios que esta
    herramienta brinda.
**- Ataque de DoS:**
    El ataque DoS se desarrolló en el lenguaje python 3 utilizando las bibliotecas
    socks y sockets para la elaboración de los sockets que se utilizarán para
    realizar las consultas y la biblioteca threading para crear los hilos que
    ejecutan la consulta.
    Herramientas:
       ● Atom
       ● Python 3
**- General:**
    En general para poder realizar la documentación correctamente se utilizó el
    programa LaTeX con el fin de seguir las instrucciones del enunciado del
    proyecto, se usó además SmartGit para que todos los integrantes del grupo
    pudieran colaborar en el código del proyecto y Google Drive para poder
    realizar la documentación en grupo y eficientemente.


## 3. Estructuras de datos usadas y funciones

Los pasos para poder realizar una clonación de un sitio web y realizar un ataque de
phishing son los siguientes:

Primero se debe descargar e instalar Tor Browser, luego se debe ir a la página de
inicio de sesión de Facebook, dar click derecho en un espacio libre y seleccionar la
opción “Ver código fuente de página”.

Se va a abrir una pestaña nueva, se selecciona todo y se copia, se pueden usar los
comandos ctrl + a y luego ctrl + c para hacerlo más rápido.


Se pega el código en un documento en bloc de notas o en un editor de texto que se
va a guardar con el nombre “index.html”.

En el caso de pegar el código en un editor de texto como Sublime Text, se usa el
atajo ctrl + f para buscar y se pone lo siguiente “action=https” donde se va a
encontrar un action que apunta a la URL de Facebook, esto se va a sustituir por un
archivo que se va a llamar “next.php”. El método post también se va a cambiar por
un get.


El código va a quedar de la siguiente forma.

Luego hay que crear un documento llamado “next.php”, la petición del login de
Facebook se va a redirigir a este script, en el header se pone la dirección de la
página real de Facebook para que redirija a esa cuando el usuario mete las
credenciales.

Luego se crea un documento .txt en el bloc de notas llamado “clon.txt” y se guarda
en blanco.


Hay que ir a la carpeta que se creó al instalar Tor Browser en Windows y dirigirse al
archivo torrc.

Se abre el archivo con el bloc de notas y se pegan las siguientes líneas.

Ahora hay que dirigirse a la carpeta que se especificó en el archivo anterior, a
tor_service. Se van a encontrar dos documentos, hostname va a tener el URL del
sitio web, en este caso “p44qes6n75d4ot72.onion” y private_key que tiene la llave
privada que no se debe compartir con nadie.

Al acceder con ese URL a Tor Browser se va a acceder a la página de
WampServer, teniendo levantados los servicios con anterioridad. Hay que ir a la
parte de phpMyAdmin para crear la siguiente base de datos con el usuario root y la
contraseña root.


Luego se crea el archivo “connection.php” para poder conectar con la base de
datos.

Todos esos archivos van a estar pegados en la carpeta www de WampServer,
dentro de una carpeta llamada Clon.

Ahora desde Tor Browser, se debe acceder al sitio web
“p44qes6n75d4ot72.onion/Clon” que será el clon de la página de Facebook, el cuál
tiene el mismo aspecto.


Ahora hay que loguearse al Facebook falso usando cualquier credencial, por
ejemplo holamundo@hotmail.com y contraseña holamundo.

Al tratar de ingresar, redirige a la página real de Facebook, como si se hubiera
puesto mal el correo o la contraseña.

El siguiente paso revisar la base de datos en phpMyAdmin para saber si las


credenciales que dio el usuario para registrarse fueron guardadas.

Los pasos para poder realizar ataque DoS al sitio web que va a estar en un hidden
service, son los siguientes:


## 4. Instrucciones para ejecutar el programa

**- Ejecutar un ataque de phishing:**
    Primero hay que levantar todos los servicios de WampServer, que actuará
    como servidor para tener el sitio web en el hidden service.
    La persona que tiene esa computadora va a pasarle el link del sitio web que
    será el clon para que otra persona desde otra computadora pueda acceder.
    Al entrar al Facebook falso podrá intentar loguearse, al darle OK el sitio web
    falso lo redirigirá al Facebook verdadero, haciendo pensar que la persona
    ingresó mal las credenciales o que hubo algún tipo de error.
    La persona que tiene la computadora con el WampServer y el sitio web
    corriendo podrá consultar la base de datos para saber si las credenciales se
    han almacenado correctamente.


**- Ejecutar un ataque de DoS:**
    Ubicado en el directorio donde se encuentra el archivo stress.py, debe
    ejecutar la siguiente línea:

```
$ python3 stress.py -n [# hilos] -r [# repeticiones] -u [url]
```
```
Parámetros:
● Número de hilos.
● Número de repeticiones por hilo
● URL (obligatorio)
```
## 5. Actividades realizadas por estudiante

**Luis Alejandro Castaing:**

- Clon: Realizar la investigacion de como se realiza un clon para hacerlo en conjunto con el compañero Luis Carlos.
    - Duracion: 1 hora 
    - Fecha: 25-10-18

- Phishing: Realizar pruebas de lo que hizo el compañero Luis Carlos para verificar su funcionamiento
    - Duracion: 4 horas 
    - Fecha: 1-10-18

- Hidden Service: Reali<ar pruebas para verificar el acceso correcto al clon realizado
    - Duracion: 1 hora 
    - Fecha: 2-10-18

- Documentacion:  Se trabaja en conjunto con los demás compañeros en el documento para terminar con el proyecto 
    - Duracion: 1 hora
    - Fecha: 7-10-18

Total de horas: 6 horas.

**Luis Carlos Sánchez:**

- Clon: Realizar el clon a la página de Facebook para que luciera igual a la original 
    - Duracion: 2 horas 30 minutos
    - Fecha: 26-9-18

- Phishing: Se realizo un ataque de phishing obteniendo los credenciales de la persona y guardandolos en una base de datos
    - Duración: 7 horas
    - Fecha: 29-9-18 y 30-8-18

- Hidden Service: Subir el sitio web falso a un hidden service mediante TOR 
    - Duracion: 2 horas
    - Fecha: 2-10-18

- Documentacion:  Se trabaja en conjunto con los demás compañeros en el documento para terminar con el proyecto 
    - Duracion: 4 horas
    - Fecha: 7-10-18

Total de horas: 15 horas y media.

### Juan José Salas:

- Investigacion sobre DoS: Investigar sobre como montar un DoS y explicarle a mi compañero Esteban Soto como ejecutar hilos en python.
    - Duracion: 2 horas
    - Fecha: 03-10-18

- Elaboración del DoS: Luego de investigar en conjunto con mi compañero Esteban Soto elaboramos el DoS sin mayor dificultad.
    - Duracion: 4 horas 
    - Fecha: 04-10-18

- Documentacion:  Se trabaja en conjunto con los demás compañeros en el documento para terminar con el proyecto 
    - Duracion: 2 horas
    - Fecha: 7-10-18
Total de horas: 8 horas

### Esteban Soto:

- Investigacion sobre DoS: Investigar junto con mi compañero Juan José sobre DoS y escuchando una explicacion rápida sobre hilos en python por eĺ
    - Duracion; 2 horas
    - Fecha: 03-10-18

- Elaboración del DoS: Luego de investigar en conjunto con mi compañero Juan José elaboramos el DoS sin mayor dificultad.
    - Duracion: 4 horas 
    - Fecha: 04-10-18

- Documentacion:  Se trabaja en conjunto con los demás compañeros en el documento para terminar con el proyecto 
    - Duracion: 2 horas
    - Fecha: 7-10-18

Total de horas: 8 horas 

## 6. Comentarios finales

El proyecto se pudo realizar de forma satisfactoria. La clonación de la página
Facebook funciona perfectamente, el ataque de phishing también funciona donde el
usuario ingresa las credenciales para loguearse y estas son guardadas en la base
de datos MySQL. El ataque DoS también funciona correctamente donde se le puede
agregar por parámetros la cantidad de hilos a ejecutar en paralelo y la cantidad de
repeticiones para que funcione la prueba de estrés.
Por el momento no se han encontrado problemas con el proyecto, todo funciona
bien. Pero hubo varias limitaciones en su momento, por ejemplo no se podían
guardar las credenciales en una base de datos, sólo en un bloc de notas. Por lo que
se tuvo que hacer una modificación y crear varios archivos para poder guardar los
datos en la base de datos. Además al principio no se podía abrir bien la página falsa
de Facebook por un problema con las rutas de WampServer. Al final se logró
arreglar todos los errores y problemas encontrados para que el programa funcione
exitosamente.
Con respecto al DoS también se logró alcanzar su funcionalidad al 100%, realizando
r (repeticiones) * n (cantidad de hilos) consultas a una página mediante el protocolo
HTTP. Durante el desarrollo de esto no fue posible señalar una limitación clara,
aunque sí fue difícil manejar la falta de tiempo por la carga del semestre.


## 7. Conclusiones y recomendaciones

Como conclusiones, este es un proyecto que deja mucho aprendizaje y experiencia
en seguridad informática a todos los integrantes del proyecto. Por ejemplo a dividir
tareas y trabajar eficientemente como grupo, a apoyar a los demás miembros si por
alguna razón lo logran realizar alguna tarea ofreciéndoles ayuda para terminarla.
Además en aspectos técnicos, nos ayudó a entender cómo es que funciona un
ataque de phishing, no es lo mismo leer la definición que realizar uno. Las personas
deben tener mucho cuidado mientras navegan por Internet ya que hay muchas
páginas que simulan ser otras por lo que las personas pueden dar por error sus
credenciales a alguien más y resultar estafados. Principalmente tener cuidado con
páginas como de bancos.
Como recomendaciones, las personas deben tener cuidado y saber cuáles son
algunos detalles que se deben diferenciar a la hora de estar en la web. En el caso
de este trabajo, se hizo un clon de Facebook. Una manera de evitar ser víctimas de
un ataque de phishing es recordando cuál es la URL correcta de cada sitio, las
personas pueden tener marcados los sitios a los que ingresan más a menudo como
favoritos. Por lo que si llega por ejemplo un correo con un link para acceder a
Facebook ellos podrán saber si se trata de una estafa o es un correo real de parte
de ellos. No pueden existir nombres de dominios iguales, en el caso de Facebook es
[http://www.facebook.com](http://www.facebook.com) pero alguien podría crear un dominio similar como
[http://www.facebook.es](http://www.facebook.es) donde muchas personas no se fijan en esos detalles y terminan
siendo víctimas de algún ataque o robo de credenciales. Además muchas veces el
diseño de la página falsa no es totalmente igual, alguna imagen podría estar más al
lado, podrían haber algunos símbolos extraños, etc, por lo que solo se debe tener
cuidado con esos detalles.


## 8. Bibliografía

A, Esaú. (2015). Hacking tutorial: Phishing en Facebook. OpenWebinars.
Recuperado de ​https://openwebinars.net/blog/hacking-tutorial-phishing-en-facebook/
F, Yúbal. (2016). Cómo registrar y gestionar nuestro dominio .onion en la deep web.
GENBETA. Recuperado de
https://www.genbeta.com/a-fondo/como-se-registran-y-gestionan-los-dominios-en-la-
deep-web
M, Luis. (2014). Como Instalar tu propio dominio .onion y tener tu sitio web en TOR.
Como Instalar Linux. Recuperado de
https://www.comoinstalarlinux.com/como-instalar-tu-propio-dominio-onion-y-tener-tu-
sitio-web-en-tor/
Chuiso. (2013). Como hacer ataques DDoS – Nivel principiante en CMD.
Chuiso.com. Recuperado de ​https://chuiso.com/como-hacer-ataques-ddos/
A, Esaú. (2015). Hacking tutorial: Cómo hacer ataque DDoS. OpenWebinars.
Recuperado de
https://openwebinars.net/blog/hacking-tutorial-como-hacer-ataque-ddos/
L, Águeda. (2016). El phishing como un servicio: esta web permite hacerlo a
cualquiera sin conocimientos técnicos. GENBETA. Recuperado de
https://www.genbeta.com/seguridad/el-phishing-como-un-servicio-esta-web-permite-
hacerlo-a-cualquiera-sin-conocimientos-tecnicos



