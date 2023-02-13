"""1. Campus requiere administrar algunos datos de sus Campers
como por ejemplo, la creación, eliminación o búsqueda de los
developers, entre otros, por tal razón, ha solicitado el diseño de
un programa que cuente con el siguiente menú como panel de
control:"""

from os import system

dbCampusArtemis = [{"nombreArtemis":"","apellidoArtemis":""}]
dbCampusSputnik = [{"nombreSputnik":"","apellidoSputnik":""}]

def AgregarCamperArtemis(camperArtemis):
    cantidadCampers = int(input("Cuantos campers desea agregar: "))
    for x in range(cantidadCampers):
        nombreArtemis = input("Ingrese el nombre del camper: ")
        apellidoArtemis = input("Ingrese el apellido del camper: ")
        camperDic={"nombreArtemis":nombreArtemis,"apellidoArtemis":apellidoArtemis}
        dbCampusArtemis.append(camperDic)
    
def EliminarCamperArtemis(camperArtemis):
    nombreArtemis= input("Ingrese el nombre del camper a eliminar: ")
    for nombreArtemis in dbCampusArtemis:
        if(nombreArtemis["nombreArtemis"] == nombreArtemis):
            dbCampusArtemis.remove(nombreArtemis)
            
def ModificarCamperArtemis(camperArtemis):
    nombreArtemis = input("Ingrese el nombre del camper a modificar: ")
    for nombreArtemis in dbCampusArtemis:
        if(nombreArtemis["nombreArtemis"] == nombreArtemis):
            nombreArtemis = input("Ingrese el nombre del camper: ")
            apellidoArtemis = input("Ingrese el apellido camper: ")
            nombreArtemis["nombreArtemis"] = nombreArtemis
            nombreArtemis["apellidoArtemis"] = apellidoArtemis

def ObtenerCamperArtemis(camperArtemis):
    for nombreArtemis in dbCampusArtemis:
        if(nombreArtemis["nombreArtemis"] == nombreArtemis):
            print(nombreArtemis)

def AgregarCamperSputnik(camperSputnik):
    cantidadCampers1 = int(input("Cuantos camper desea agregar: "))
    for x in range(cantidadCampers1):
        nombreSputnik = input("Ingrese el nombre del camper: ")
        apellidoSputnik = input("Ingrese el apellido del camper: ")
        camperDic1={"nombreSputnik":nombreSputnik,"apellidoSputnik":apellidoSputnik}
        dbCampusSputnik.append(camperDic1)
    
def EliminarCamperSputnik(camperSputnik):
    nombreSputnik= input("Ingrese el nombre del a eliminar: ")
    for nombreSputnik in dbCampusSputnik:
        if(nombreSputnik["nombreSputnik"] == nombreSputnik):
            dbCampusSputnik.remove(nombreSputnik)
            
def ModificarCamperSputnik(camperSputnik):
    nombreSputnik = input("Ingrese el nombre del camperSputnik a modificar: ")
    for nombreSputnik in dbCampusSputnik:
        if(nombreSputnik["nombreSputnik"] == nombreSputnik ):
            nombreSputnik = input("Ingrese el nombre del camper : ")
            apellidoSputnik = input("Ingrese el apellido camper : ")
            nombreSputnik["nombreSputnik"] = nombreSputnik
            nombreSputnik["apellidoSputnik"] = apellidoSputnik

def ObtenerCamperSputnik(camperSputnik):
    for nombreSputnik in dbCampusSputnik:
        if(nombreSputnik["nombreSputnik"] == nombreSputnik):
            print(nombreSputnik)

while True:
    print("----------------------MENU-------------------------\n"
    "\t 1. CREAR GRUPO ARTEMIS:\n"
    "\t1.1 LISTAR CAMPERS DE ARTEMIS:\n"
    "\t1.2 AGREGAR CAMPERS A ARTEMIS:\n"
    "\t1.3 ELIMINAR CAMPERS DE ARTEMIS:\n"
    "\t1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS:\n"
    "\t1.5 BUSCAR CAMPERS EN LISTA DE ARTEMIS:\n"
    "\t 2. CREAR GRUPO SPUTNIK:\n"
    "\t2.1 LISTAR CAMPERS DE SPUTNIK:\n"
    "\t2.2 AGREGAR CAMPERS A SPUTNIK:\n"
    "\t2.3 ELIMINAR CAMPERS DE SPUTNIK:\n"
    "\t2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK:\n"
    "\t2.5 BUSCAR CAMPERS EN LISTA DE SPUTNIK:\n"
    "\t 3. SALIR"
    )

        
    opcion = float(input("Seleccione una opcion: "))
    if(opcion == 1):
        AgregarCamperArtemis("camperArtemis")
    elif(opcion==1.1):
        print(dbCampusArtemis)
    elif(opcion==1.2):
        AgregarCamperArtemis("camperArtemis")
    elif(opcion==1.3):
        EliminarCamperArtemis("camperArtemis")
    elif(opcion==1.4):
        lista1 = sorted(dbCampusArtemis, key=lambda x: x['nombreArtemis'])
        print("\nOrdenado por 'nombreArtemis'")
        print(lista1)
    elif(opcion==1.5):
        ObtenerCamperArtemis("nombreArtemis")
    elif(opcion == 2):
        AgregarCamperSputnik("nombreSputnik")
    elif(opcion==1.1):
        print(dbCampusSputnik)
    elif(opcion==1.2):
        AgregarCamperSputnik("nombreSputnik")
    elif(opcion==1.3):
        EliminarCamperSputnik("nombreSputnik")
    elif(opcion==1.4):
        lista2 = sorted(dbCampusSputnik, key=lambda x: x['nombreSputnik'])
        print("\nOrdenado por 'nombreSputnik'")
        print(lista2)
    elif(opcion==1.5):
        ObtenerCamperSputnik("nombreSputnik")