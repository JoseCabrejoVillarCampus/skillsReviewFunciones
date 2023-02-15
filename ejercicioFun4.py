"""4. Una empresa tiene 500 almacenes. Cada almacén debe
reportar el nombre y 5 registros c/u, contiene el tipo de articulo
y el número de unidades vendidas de ese artículo.
Haga un programa en Python para determinar cuál fue el
almacén que mas vendió, cual fue el articulo más vendido de
ese almacén y cual el más vendido en general"""


def ventasAlmacen():
    dbRegistros={}
    numeroRegistros = 5
    listSum=0
    for x in range(numeroRegistros):
        tipoArticulo = input("\nIngrese el Tipo de Articulo: ")
        numeroVentas= int(input("Ingrese el Número de Unidades Vendidas: "))
        ventasDic={"articulo":tipoArticulo,"cantidad":numeroVentas}
        dbRegistros[tipoArticulo,numeroVentas]=ventasDic
        totalVentas
ventasAlmacen()

"""ordenados = sorted(dbRegistros, key=lambda  ventas : ventas[1])
        print(ordenados)"""
