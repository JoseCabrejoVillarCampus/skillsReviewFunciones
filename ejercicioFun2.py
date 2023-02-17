"""2. N atletas han pasado a finales en salto triple en los juegos
olímpicos de 2022.
Diseñe un programa que pida por teclado los nombres de cada
atleta finalista y a su vez, sus marcas del salto en metros.
Informar el nombre de la atleta campeona que se quede
con la medalla de oro y si rompió récord, reportar el pago que
será de 500 millones. El récord esta en 15,50 metros"""




def AgregarAtletas():
    atletas=[]
    marcas=[]
    record=15.50
    print("\n\n...............Registro Salto triple.....................\n")
    cantidadAtletas = int(input("\nCuantos atletas desea agregar: "))
    for x in range(cantidadAtletas):
        atletas.append(input("Ingrese el nombre del atleta: "))
        marcas.append(float(input("Ingrese la marca del atleta: ")))
        
        
    union=(list(zip(atletas,marcas)))
    union=sorted(union, key=lambda union:union[1], reverse=True)    
    
    print(union)
    if union[0][1]>record:
        print("el atleta",union[0] ,"rompió el récord el pago queserá de 500 millones")
AgregarAtletas()
