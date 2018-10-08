## Ataque DoS

#### Introducción

Es necesario realizar una prueba de estrés para ello debe crear una herramienta que realice  N  consultas  HTTP  en  paralelo  utilizando  hilos  ysockets. El programa de ataque recibirá como parámetro lacantidad de hilos a ejecutar en paralelo y la cantidadde repeticiones. Luego cada hilo abrirá un socket TCP hacia el hidden service y realizará una consulta utilizando el método GET. La sintaxis del stress es:


`$ python3 stress.py -n [# hilos] -r [# repeticiones] -u [url]`


#### Ambiente de desarrollo

El ataque DoS se desarrolló en el leguaje python3 utilizando las bibliotecas socks y sockets para la elaboración de los sockets que se utilizarán para realizar las consultas y la biblioteca threading para crear los hilos que ejecutan la consulta.

Herramientas:
- Python3
- Atom

#### Funciones y estructuras de datos
La función de ataque es el objetivo que posee cada hilo, consulta la variable con la cantidad de repeticiones y realiza la consulta HTTP.

| Nombre de la función | Descripción                    |
| :---------------: | :---------------: |
| `ataque(id, client)`      | Esta funcion perpetra el ataque y está asociada con cada hilo.   |


```python
def ataque(id, client):
    mensaje = "GET / HTTP/1.1\r\nHost: " + url + "\r\n\r\n"

    for i in range(cantidad_repeticiones):

        client.sendall(mensaje.encode('utf-8'))
        print("Hilo %10d solicitando por %10d vez." % (id+1, i+1))

```
No se utilizaron más funciones ni estructuras de datos relevantes para el ataque.

#### Instrucciones para ejecutar el programa

Ubicado en el directorio donde se encuentra el archivo `stress.py`, debe ejecutar la siguiente línea:

`$ python3 stress.py -n [# hilos] -r [# repeticiones] -u [url]`

Parámetros:
- Número de hilos.
- Número de repeticiones por hilo.
- URL (obligatorio).


#### Comentarios finales

El programa se logró completar en su totalidad y es 100% funcional, realizando r (repeticiones) * n (cantidad de hilos) consultas a una página mediante el protocolo HTTP.

#### Conclusiones y recomendaciones

El programa es sencillo de realizar, ya que no requiere de mucho conocimiento técnico para llevarlo a cabo. Existen distintas maneras para realizar el ataque, ya sea mediante las bibliotecas socks y socket o la biblioteca request. 

Utilizar la segunda facilita significativamente el proceso, ya que se ahorra la realización de un socket y la especificación del mensaje que se va a enviar al servidor; sin embargo, como el profesor solicitó un socket y protocolo TCP de comunicación, se debió realizar cambios, complicando un poco más las cosas.
