"""4. Una empresa tiene 500 almacenes. Cada almacén debe
reportar el nombre y 5 registros c/u, contiene el tipo de articulo
y el número de unidades vendidas de ese artículo.
Haga un programa en Python para determinar cuál fue el
almacén que mas vendió, cual fue el articulo más vendido de
ese almacén y cual el más vendido en general"""



def ventasAlmacen():
    dbRegistros={}
    print("\n\n----------------!Bienvenido¡--------------------\n")
    numeroAlmacenes = int(input("\nPor favor Ingrese el Número de Almacenes: "))
    for i in range(numeroAlmacenes):
            nombreAlmacen=input(f"Ingrese el nombre del Almacen {i+1}: ")
            nRegistros=int(input("\nPor favor Ingrese cantidad de Registros: "))
            for x in range(nRegistros):
                articulo = input(f"Ingrese el Primer Tipo de Articulo {i+1}: ")
                numeroVendido= int(input("Ingrese la cantidad del articulo vendido: "))
                if nombreAlmacen in dbRegistros:
                    if articulo in dbRegistros[nombreAlmacen]:
                        dbRegistros[nombreAlmacen][articulo] +=numeroVendido
                    else : dbRegistros[nombreAlmacen][articulo] =numeroVendido
                else:dbRegistros[nombreAlmacen]={articulo: numeroVendido}
    
    almacenMayorVentas=""
    almacenMayorVentasToTAL=0
    for nombreAlmacen, numeroVendido in dbRegistros.items():
        almacenMayorVentas= sum(numeroVendido.values())
        if almacenMayorVentas > almacenMayorVentasToTAL:
             almacenMayorVentasToTAL= almacenMayorVentas
             almacenMayorVentas= nombreAlmacen

    print("El almacen con mayor ventas fue: ", almacenMayorVentas)
    print("con un Total de:" ,almacenMayorVentasToTAL)
ventasAlmacen()