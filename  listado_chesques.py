#defino librerias a utilizar
import sys,csv
import argparse

#defino constantes y variables a utilizar
parser = argparse.ArgumentosParser(description="Just an example", formatter_class=argparse.ArgumentDefaultsHelpFormat)
opciones = """
Bienvenido al programa de control de cheques
--------------------------------------------
Por favor seleccione una opcion
1. Cargar un nuevo cheque
2. Buscar un cheque por DNI
3. Salir
"""
runtime = True

#defino funciones
def readFile():
    cheques = []
    file = open(str(parser.parse_args().file),"r")
    csvfile = csv.reader(file)
    for row in csvfile:
        if row != []:
            data = {"NroCheque":row[0],"CodigoBAnco":row[1],"CodigoSucursal":row[2],
            "NumeroCuentaOrigen":row[3],"NumeroCuentaDestino":row[4],"Valor":row[5],
            "FechaOrigen":row[6],"FechaPago":row[7],"DNI":row[8],"Tipo":row[9],"Estado":row[10]}
            cheques.append(data)
    file.close()
    return cheques

def buscarPorDni (dni):
    busqueda = []
    cantidad = 0
    cheques = readFile()
    for cheque in cheques:
        if cheque["DNI"] == dni:
            cantidad +=1
            print("cheque encontrado")
            busqueda.append(cheque)
    print(f"Se encontraron {cantidad} de cheuques")
    return busqueda



if __name__ == "__main__":
    parser.add_argument("-f","--file",help="Nombre del archivo csv")
    parser.add_argument("-dni","--dni",help="DNI del cliente donde se filtaran")
    parser.add_argument("-s","--salida",help="Salida: PANTALLA o CSV")
    parser.add_argument("-t","--tipo",help="Tipo de cheque: EMITIDO o DEPOSITADO")
    print("Archivo: ", parser.parse_args().file)
    print("DNI: ", parser.parse_args().dni)
    print("Salida seleccionada: ", parser.parse_args().salida)
    print("Salida seleccionada: ", parser.parse_args().tipo)

    dni = int(parser.parse_args().dni)
    salida = str(parser.parse_args().salida)
    readFile()
    if salida == "PANTALLA":
        print(readFile())
    else:
        print("grabando archivo")
        
