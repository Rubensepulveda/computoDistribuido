#importamos las librerias necesarias
import tornado.ioloop
import gevent.monkey
from tornado.httpclient import AsyncHTTPClient
import gevent.monkey
from urllib2 import urlopen
#Esta libreria es para limpiar la pantalla
from IPython.display import clear_output

#Declaramos el metodo de Menu
def menu():
    #metodo para limpiar el menu
    clear_output()
    print("\t----------MENU------ \n")
    print("\t1- Estilo Green")
    print("\t1- Estilo Callback")
    print("\t3- Salir ")

#Iniciamos un ciclo while anidado
while True:
    #Invocamos al metodo del menu
    menu()

    #solicitamos una opcion al usuario y lo guardamos en la vairable opcionMenu
    opcionMenu= raw_input("Escoger una opcion>> ")

    if opcionMenu== "1":
        clear_output()
        print("")
        print("***Estilo Green*** \n")
        #declaramos un metodo de la libreria gevent
        gevent.monkey.patch_all()
        #declaramos la lista de trabajo
        urls = []
        #declaramos la variable donde guardaremos la cantidad de urls
        x = int(raw_input("ingrese cantidad de urls "))
        #usamos un ciclo for para llenar la lista
        for i in range(x):
             hola = i+1
             num = raw_input("ingrese url %d :"%hola)
             urls.append(num)
        #declaramos el metodo para realizar el miltihilo
        def print_head(url):
            #en esta parte se toma la url y se le da formato
            print('Starting {}'.format(url))
            #declaramos la variable data donde la usamos para leer y abrir la url
            data = urlopen(url).read()
            print('{}: {} bytes: {}'.format(url, len(data), data))
        #aqui empezamos el tomar las urls para empezar a hacer el hilo
        jobs = [gevent.spawn(print_head, _url) for _url in urls]
        #empezamos a disparar las urls recibidas
        gevent.wait(jobs)
        a=raw_input("\n Quieres regresar al menu principal y=si?: ")
        if a=="y":
            menu()
        else :
            pass
    elif opcionMenu== "2":
        clear_output()
        print("")
        print("***Estilo Callback*** \n")
        #Declaramos la lista
        urls = []
        #Declaramos la variable x donde se guardara la cantidad de urls
        x = int(raw_input("ingrese la cantidad de urls de trabajo "))
        #comienza el ciclo for para recorrer la cantidad de url antes ingresada
        for i in range(x):
            hola = i+1
            #En la variable num guardamos la url que el usuario ingrese
            num = raw_input("ingrese url %d :"%hola)
            #con el metodo .append estamos ingresando las url a lista
            urls.append(num)

        def handle_response(response):
            if response.error:
                print("Error:", response.error)
            else:
                url = response.request.url
                data = response.body
                print('{}: {} bytes: {}'.format(url, len(data), data))

        http_client = AsyncHTTPClient()
        for url in urls:
            http_client.fetch(url, handle_response)
    
        tornado.ioloop.IOLoop.instance().start()
        #tornado.ioloop.IOLoop.instance().stop()
        
        a=raw_input("\n Quieres regresar al menu principal y=si?: ")
        if a=="y":
            menu()
        else :
            pass
    elif opcionMenu == "3":
        break
    else:
        raw_input("no has seleccionado una opcion valida  \npulsa la tecla enter para continuar")
