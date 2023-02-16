"""4. Una empresa tiene 500 almacenes. Cada almacén debe
reportar el nombre y 5 registros c/u, contiene el tipo de articulo
y el número de unidades vendidas de ese artículo.
Haga un programa en Python para determinar cuál fue el
almacén que mas vendió, cual fue el articulo más vendido de
ese almacén y cual el más vendido en general"""


def ventasAlmacen():
    dbRegistros={}
    numeroAlmacenes = int(input("\nIngrese el Número de Almacenes:"))
    for x in range(numeroAlmacenes):
        nombreAlmacen=input("Ingrese el nombre del Almace: ")
        tipoArticulo1 = input("Ingrese el Primer Tipo de Articulo: ")
        numeroVentas1= int(input("Ingrese el Número de Unidades Vendidas: "))
        tipoArticulo2 = input("Ingrese el Segundo Tipo de Articulo: ")
        numeroVentas2= int(input("Ingrese el Número de Unidades Vendidas: "))
        tipoArticulo3 = input("Ingrese el Tercer Tipo de Articulo: ")
        numeroVentas3= int(input("Ingrese el Número de Unidades Vendidas: "))
        tipoArticulo4 = input("Ingrese el Cuarto Tipo de Articulo: ")
        numeroVentas4= int(input("Ingrese el Número de Unidades Vendidas: "))
        tipoArticulo5 = input("Ingrese el Quinto Tipo de Articulo: ")
        numeroVentas5= int(input("Ingrese el Número de Unidades Vendidas: "))
        ventasDic={"almacen":nombreAlmacen,"articulo1":tipoArticulo1,"cantidad1":numeroVentas1,"articulo2":tipoArticulo2,"cantidad3":numeroVentas3,"articulo4":tipoArticulo4,"cantidad4":numeroVentas4,"articulo1":tipoArticulo1,"cantidad5":numeroVentas5}
        dbRegistros[nombreAlmacen,tipoArticulo1,numeroVentas1,tipoArticulo2,numeroVentas2,tipoArticulo3,numeroVentas3,tipoArticulo4,numeroVentas4,tipoArticulo5,numeroVentas5]=ventasDic
        ordenados = sorted(dbRegistros, key=lambda  ventas : ventas[1])
        print(ordenados)
ventasAlmacen()

