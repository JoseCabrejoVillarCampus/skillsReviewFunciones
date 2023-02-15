"""3. En pocos días comienza la vuelta a España y la federación
colombiana de ciclismo, como incentivo ha determinado pagar
un valor adicional. El programa pedirá por teclado el sueldo
básico por kilometro recorrido, el número de kilómetros
recorridos durante toda la vuelta, numero de kilómetros
recorridos con la camiseta de líder.
Calcular el valor a pagar total, si se sabe que si recorre en la
bici más de 1800 kilómetros con la camiseta de líder, esos
kilómetros se consideran especiales y tendrán un recargo de
25%.
El total de kilómetros por recorrer durante toda la vuelta serán
3.277 kilómetros,el ganador de la vuelta a España recibirá 700
millones de pesos."""



def valorTotal():
    nciclistas = int(input("\nCuantos ciclistas desea liquidar: "))
    for x in range(nciclistas):
        sueldoBasico=3277*float(input("Ingrese sueldo básico por kilometro recorrido: "))
        numeroKilometrosLider=float(input("Ingrese el número de kilómetros recorridos con la camiseta de líder:"))
        if numeroKilometrosLider>1800:
            print(sueldoBasico+(sueldoBasico*0.25))
        else:
            print(sueldoBasico)

valorTotal()