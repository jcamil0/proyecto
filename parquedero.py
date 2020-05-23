#titulo: parqueadero.py
#descripcio: sistema de administracion de parqueo desarrolaldo en el lenguaje de programacion python para la universidad PUJ
#autor: laura
#version: 0.1
#version de python : 3.6.9
#===========================================================================================================================

import json
import  os
import time

pisos = {}
usuarios={}
aux = []
#usuarios['usuarios'] = []

vehuculos=['vehuculo', 'motocicleta' ,'eléctrico','Discapacitado']
tipo_usuario=['Estudiante', 'Personal Adminstrativo' ,'Profesores']
planes=['mensualidad','diario']


#funcion que abre  el archivo json de los psisos
def archivo_pisos():
    try:
        with open('pisos.json') as archivo:
            pisos = json.load(archivo)
        #Itera a través de cada sublista en su lista original y lo descomprime  en la llamada impresa con *
        #for i in pisos:
         #   print("          ",i)
          #  for j in pisos[i]:
           #     print(*j)
        return pisos
    except IOError as e:
        print ("el archivo no se encuentra en el directorio ",e)

def archivoUsuarios():
    try:
        with open('usuarios.json') as archivo:
            usuarios = json.load(archivo)

    except IOError as e:
        print("el archivo ususrios no se encuentra en el directorio ", e)
    return usuarios

def banner():
    dibujo = open("archivo.txt")
    for i in dibujo:
        print(dibujo.read())

def despedida():
    dibujo = open("despedida.txt")
    for i in dibujo:
        print(dibujo.read())



#regusstro de estudiantes,profesores o  del personal administrativo
def registros(usuarios):
    print("            REGISTRO")
    print("\n")

    Nombre=input(str("        NOMBRE: "))
    Apellido=input(str("        APELLIDO: "))
    NombresApellido = Nombre+" "+Apellido
    Id = int(input("        ID: "))
    duplicados(Id,usuarios)
    TipodeUsuario = tipousuario()
    Placa = input(str("         PLACA: "))
    #VerificarPlaca(NombresApellido,Id,Placa,usuarios)
    verificarParquederos(archivo_pisos())
    TipoVehuculo = tipo_vehiculo()
    Plan=tipo_plan()
    aux.append([NombresApellido, Id, TipodeUsuario, Placa, TipoVehuculo,Plan])

    usuarios['usuarios'] += aux
    with open('usuarios.json', 'w') as file:
            json.dump(usuarios,file,sort_keys=False,separators=(',', ':'),indent=4)

def tipo_vehiculo():
    print("""
            1) vehuculo       3) auto electrico
            2)  motocicleta       4) discapacitado
            """)
    # Leemos lo que ingresa el usuario
    eligio = input("Selecciona algo :")
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
    eligio = input("Selecciona algo :")
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



def duplicados(Id,usuarios):
    for i in usuarios:
        for j in usuarios[i]:
            if j[1] == Id:
                print("ESTE USUSARIO YA SE ENCUENTRA REGISTRADO")
                time.sleep(3)
                os.system("clear")
                return registros(usuarios)
            else:
                continue

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
    #valors=[]
    #for value in pisos.values():
     #   print(value)
    valores = pisos
    for i in pisos:
        print("          ",i)
        for j in pisos[i]:
            print(j)



    for i in valores:
        for j in valores[i]:
            print()



    eleigio=int(input("en que piso desea parquear"))

    for name, datalist in pisos.items():
        for datadict in datalist:
            for key, value in datadict.items():
                if eleigio == 1:
                    datadict[key] = "XXxxxxxxxxxxxxX"
                    break


def Pisos(pisos, tipo):
    print()

def reporte():
    print()

def menu():
    salir = False
    while not salir:
        banner()
        print("""
         1)REGISTAR VEHUCULO      3)estdisticas 
         2)                       4)Salir
            """)
        # Leemos lo que ingresa el usuario
        eligio=input("           Selecciona algo :")
        # Según lo que ingresó, código diferente
        if eligio=="1":
            os.system("clean")
            registros(archivoUsuarios())
        elif eligio=="2":
            print("..")
        elif eligio=="3":
            print("..")
        elif eligio=="4":
            despedida()
            salir = True
        else:
            print("Opción no válida")
            os.system("clean")





menu()
