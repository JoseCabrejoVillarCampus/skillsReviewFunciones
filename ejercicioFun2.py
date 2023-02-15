"""2. N atletas han pasado a finales en salto triple en los juegos
olímpicos de 2022.
Diseñe un programa que pida por teclado los nombres de cada
atleta finalista y a su vez, sus marcas del salto en metros.
Informar el nombre de la atleta campeona que se quede
con la medalla de oro y si rompió récord, reportar el pago que
será de 500 millones. El récord esta en 15,50 metros"""




def AgregarAtletas():
    atletasMarcas={}
    cantidadAtletas = int(input("\nCuantos atletas desea agregar: "))
    for x in range(cantidadAtletas):
        nombre = input("Ingrese el nombre del atleta: ")
        marca= float(input("Ingrese la marca del atleta: "))
        atletaDic={"nombre":nombre,"marca":marca}
        atletasMarcas[nombre,marca]=atletaDic
        if (marca>15.50):
            print ("El Atleta rompio el record de 15.50 metros \n el pago que será de 500 millones")
        ordenados = sorted(atletasMarcas, key=lambda  metros : metros[0])
        print(ordenados)
AgregarAtletas()
