"""1. Campus requiere administrar algunos datos de sus Campers
como por ejemplo, la creación, eliminación o búsqueda de los
developers, entre otros, por tal razón, ha solicitado el diseño de
un programa que cuente con el siguiente menú como panel de
control:"""


opcion=''
while opcion!=3:
    print("----------------------MENU-------------------------\n"
    "\t 1. CREAR GRUPO ARTEMIS:\n"
    "\t1.1 AGREGAR CAMPERS A ARTEMIS:\n"
    "\t1.2 LISTAR CAMPERS DE ARTEMIS:\n"
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


    opcion = input("Porfavor ingresar Opcion: ")

    if opcion == '1':
        dbcampusArtemis={}
        print("grupo artemis ha sido creado")
    if opcion == '1.1':
        cantidadArtemis = int(input("Cuantos campers desea agregar a Artemis: "))
        for x in range(cantidadArtemis):
            nombre = input('Introduce el nombre del camper: ')
            direccion = input('Introduce la dirección del camper: ')
            telefono = input('Introduce el teléfono del camper: ')
            email = input('Introduce el correo electrónico del camper: ')
            camper = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email}
            dbcampusArtemis[nombre] = camper
    if opcion == '1.2':
        print('Lista de campers Artemis')
        print(dbcampusArtemis)
    if opcion == '1.3':
        nombre = input('Introduce nombre del camper: ')
        if nombre in dbcampusArtemis:
            del dbcampusArtemis[nombre]
        else:
            print('No existe el camper con el nombre', nombre)
    if opcion == '1.4':
        ordenados = sorted(dbcampusArtemis, key=lambda campers : campers[0])
        print(ordenados)
    if opcion == '1.5':
        nombre = input('Introduce nombre del camper: ')
        if nombre in dbcampusArtemis:
            print('nombre:', nombre)
            for clave, valor in dbcampusArtemis[nombre].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el camper con el nombre', nombre)
    if opcion == '2':
        dbcampusSputnik={}
        print("grupo Sputnik ha sido creado")
    if opcion == '2.1':
        cantidadSputnik = int(input("Cuantos campers desea agregar a Sputnik: "))
        for x in range(cantidadSputnik):
            nombreS = input('Introduce el nombre del camper: ')
            direccionS = input('Introduce la dirección del camper: ')
            telefonoS = input('Introduce el teléfono del camper: ')
            emailS = input('Introduce el correo electrónico del camper: ')
            camperS = {'nombre':nombreS, 'dirección':direccionS, 'teléfono':telefonoS, 'email':emailS}
            dbcampusSputnik[nombreS] = camperS
    if opcion == '2.2':
        print('Lista de campers Sputnik')
        print(dbcampusSputnik)
    if opcion == '2.3':
        nombreS = input('Introduce nombre del camper: ')
        if nombreS in dbcampusSputnik:
            del dbcampusSputnik[nombreS]
        else:
            print('No existe el camper con el nombre', nombreS)
    if opcion == '2.4':
        ordenadosS = sorted(dbcampusSputnik, key=lambda campersS : campersS[0])
        print(ordenadosS)
    if opcion == '1.5':
        nombreS = input('Introduce nombre del camper: ')
        if nombreS in dbcampusSputnik:
            print('nombre:', nombreS)
            for clave, valor in dbcampusSputnik[nombreS].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el camper con el nombre', nombreS)
    
    



