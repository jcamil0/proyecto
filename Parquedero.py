#titulo: parqueadero.py
#autor: camilo 
#version: 0.1
#version de python : 3.6.9
#===========================================================================================================================

import json #nos permite manejar archivos json como leer o escribir
import  os  #el modulo os nos permite acceder a funcionalidades dependientes del Sistema Operativo
import time #el módulo time  nos permite manejar los tiempos en nuestro programa

pisos = {}
usuarios={}
aux = []


vehuculos=['vehuculo', 'motocicleta' ,'eléctrico','Discapacitado']
tipo_usuario=['Estudiante', 'Personal Adminstrativo' ,'Profesores']
planes=['mensualidad','diario']

#variables que se suman depoendiendo el tipo de vehuculo qu ehay en el parquedero
automovil = 0
electrico = 0
motociclita = 0
discapacitado = 0

#funcion que abre  el archivo json de los pisos y retorna pisos
def archivo_pisos():
    try:
        with open('pisos.json') as archivo:
            pisos = json.load(archivo)
        return pisos
    except IOError as e:  #atrapa las excepciones detectando errores cuando el archivo no existe o tiene un error de sintaxis (JSON no válido)
        print ("el archivo PISOS no se encuentra en el directorio ",e) #impirme el mensaje y se concatena a la excepcion que arrojo

#funcion que abre  el archivo json de los ususarios y retorna usuarios
def archivoUsuarios():
    try:
        with open('usuarios.json') as archivo:
            usuarios = json.load(archivo)
    except IOError as e:    #trapa las excepciones detectando errores cuando el archivo no existe o tiene un error de sintaxis (JSON no válido)
        print("el archivo USUARIO  no se encuentra en el directorio ", e)
    return usuarios


def banner():   #abre un txt el cual tiene en su interior un asciiArt
    dibujo = open("archivo.txt")
    for i in dibujo:    #se lee linea a linea el archivo
        print(dibujo.read())

def despedida():    #abre un txt el cual tiene en su interior un asciiArt
    dibujo = open("despedida.txt")
    for i in dibujo:    #se lee linea a linea el archivo
        print(dibujo.read())

def verUsuarios(usuarios):  # imprime los ususarios que hay en el diccionario
    for i in usuarios:
        print("          ", i)
        for j in usuarios[i]:
            print(j)

#registro de los ususarios en el sistema
def registros(usuarios):
    print("            REGISTRO")
    print("\n")
    Nombre=input(str("        NOMBRE: "))
    Apellido=input(str("        APELLIDO: "))
    NombresApellido = Nombre+" "+Apellido
    Id = int(input("        ID: "))
    duplicados(Id,usuarios)
    TipodeUsuario = tipousuario()           #TipoUsuario es igual a el retornno que hizo el mentodo tipousuario()
    Placa = input(str("         PLACA: "))
    #VerificarPlaca(NombresApellido,Id,Placa,usuarios)
    verificarParquederos(archivo_pisos())
    TipoVehuculo = tipo_vehiculo()
    Plan=tipo_plan()
    aux.append([NombresApellido, Id, TipodeUsuario, Placa, TipoVehuculo,Plan])

    usuarios['usuarios'] += aux              #se concatena lo que contiene el dicioanrio original con aux
    with open('usuarios.json', 'w') as file:    #se escribe en el archivo json
            json.dump(usuarios,file,sort_keys=False,separators=(',', ':'),indent=1)

def tipo_vehiculo():
    print("""
        1) vehuculo       3) auto electrico
        2)  motocicleta       4) discapacitado
            """)
    # Leemos lo que ingresa el usuario
    eligio = input("        Selecciona algo :")
    if eligio == "1":
        return vehuculos[0]
    elif eligio == "2":
        return vehuculos[1]
    elif eligio == "3":
        return vehuculos[2]
    elif eligio == "4":
        return vehuculos[3]
    else:
        print("Opción no válida")

def tipousuario():
    print("""
        1) ESTUDINATE       3) PROFESOR
        2)  PERSONAL ADMINSTRATIVO      
            """)
    # Leemos lo que ingresa el usuario
    eligio = input("        Selecciona algo :")
    if eligio == "1":
        return tipo_usuario[0]
    elif eligio == "2":
        return tipo_usuario[1]
    elif eligio == "3":
        return tipo_usuario[2]
    else:
        print("Opción no válida")

def tipo_plan():
    print("""
            1) mensualidad       2) diario
            """)
    # Leemos lo que ingresa el usuario
    eligio = input("Selecciona algo :")
    if eligio == "1":
        return planes[0]
    elif eligio == "2":
        return planes[1]
    else:
        print("Opción no válida")


#funcion que verifica que las cedulas no se repitan
#en caso de que la cedula se repita va a retornal de nuuevo al inicio del regidtro
# si no continuara  su ejecucion en el registro
def duplicados(Id,usuarios):
    for i in usuarios:
        for j in usuarios[i]:
            if j[1] == Id:
                print("ESTE USUSARIO YA SE ENCUENTRA REGISTRADO")
                time.sleep(3)       #espera de 3 segundos para continual con la siguiente intrucion
                os.system("clear")  #una ves pasen los 3 segundos la consola se limpia
                return registros(usuarios) # en caso de hayar un elemnto que ya exista retornara de nuevo al registro
            else:
                continue # de lo contrario va  a continuar con el registro

def VerificarPlaca(nombreapellido,id,placa,usuarios):
    for i in usuarios:
        for j in usuarios[i]:
            if j[3]==placa:

                    return menu()
            else:
                print("PLACA NO ENCONTRADA")
                tipo = tipo_vehiculo()
                aux.append([nombreapellido, id, "VISITANTE", tipo, "", planes[1]])
                usuarios['usuarios'] += aux
                with open('usuarios.json', 'w') as file:
                    json.dump(usuarios, file, sort_keys=False, separators=(',', ':'), indent=4)
                break

def verificarParquederos(pisos):
    for i in pisos:
        print("          ",i)
        for j in pisos[i]:
            print(j)

    for i in pisos:
        for j in pisos[i]:
            for pisos[i] in j:
                if pisos[i]==1:
                    automovil=automovil+1
                elif pisos[i]==2:
                    electrico=electrico+1
                elif pisos[i]==3:
                    motociclita=motociclita+1
                elif pisos[i] == 4:
                    discapacitado=discapacitado+1
    print()
    print("     disponibles")
    print("     atomoviles:",automovil)
    print("     auto electrico:", electrico)
    print("     motocicleta",motociclita)
    print("     discapacitado",discapacitado)

    eleigio = int(input("   en que piso desea parquear"))






def Pisos(pisos, tipo):
    print()

def reporte():
    file = open("reporte.txt", "w")
    file.write("Primera línea\n" )
    file.write("Segunda línea")
    file.close()

def retiro(usuarios):
    print("         RETIRO DEL VEHICULO")
    tiempo=int(input("         cuantas horas estuvo en el parqeudero "))
    placa=input("           cual es la placa de su vehuculo ")

    for i in usuarios:
        for j in usuarios[i]:
            if j[1] == placa:
                print("puede hacer el retiro")

            else:
                print("vehiculo no registrado")
                return registros(archivoUsuarios())



#menu principal el cual se hace siempre y cuando salir sea false
def menu():
    salir = False
    while not salir:
        banner()
        print("""
         1)REGISTAR VEHUCULO      3)estdisticas 
         2)VER USUSARIOS          4)RETIRAR
         5) salir 
            """)
        eligio=input("           Selecciona algo :")     # Leemos lo que ingresa el usuario

        # Según lo que ingresó, código diferente
        if eligio=="1":
            os.system("clear")               #se limpia la consola
            registros(archivoUsuarios())    #funcion de registros() que recibe como parametro lo que retorna el mentodo archivo usuario
        elif eligio=="2":
            verUsuarios(archivoUsuarios())
            time.sleep(10)
            os.system("clear")
        elif eligio=="3":
            print("..")

        elif eligio=="4":
            print("..")

        elif eligio=="5":
            despedida() # metodo de el mensaje de despedida
            salir = True
        else:
            print("Opción no válida")
            os.system("clear")




reporte()
menu()
