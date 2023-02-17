"""4. Una empresa tiene 500 almacenes. Cada almacén debe
reportar el nombre y 5 registros c/u, contiene el tipo de articulo
y el número de unidades vendidas de ese artículo.
Haga un programa en Python para determinar cuál fue el
almacén que mas vendió, cual fue el articulo más vendido de
ese almacén y cual el más vendido en general"""


def ventasAlmacen():
    almacen=[]
    articulo=[]
    articuloCantidad=[]

    print("\n\n----------------!Bienvenido¡--------------------\n")
    numeroAlmacenes = int(input("\nPor favor Ingrese el Número de Almacenes: "))
    for x in range(numeroAlmacenes):
        almacen.append(input("\n\tIngrese el nombre del Almace: "))
        cantidadVendidad= int(input("\n\tIngrese la Cantidad de Articulos: "))
        for i in range(cantidadVendidad):
            articulo.append(input("\n\tIngrese el Nombre del Articulo: "))
            articuloCantidad.append(int(input("\n\tIngrese el Número de Unidades Vendidas: ")))
    
    
    union=(list(zip(almacen,articulo,articuloCantidad)))
    union=sorted(union, key=lambda union:union[0], reverse=True)
    resultado = ["En el Almacen", union[0][0] ,"Se vendio el rticulo", union[0][1], "En cantidad de",union[0][2],"unidades", "El articulo mas vendido por el almacen fue: ", max(union[0])]
    print(resultado)

ventasAlmacen()