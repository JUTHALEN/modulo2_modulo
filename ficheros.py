file_name ="C::\\Users\\Judit\\Dowloads\\fichero.csv"

try:
    file = open(file_name, "r")
    print("El fichero se ha abierto correctamente")
    '''
    #Lectura de una lina de un fichero
    linea1 = file.readline()
    print(linea1)
    '''
    #Recorrido de un fichero linea a linea
    for linea in file:
        valores = linea.split(",")
        id = valores[0]
        direccion = valores[1]
        description = valores[2]
        print(f"<record id={id}>")
        print('</record>')

except:
    print("El fichero no se ha podido abrir")
else:
    print("El fichero se ha cerrado correctamente")
    file.close()
finally:
    print("Fin del programa")