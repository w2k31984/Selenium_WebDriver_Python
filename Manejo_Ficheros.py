#Los ficheros sirven para guardar datos .csv o bien importar datos, para diferentes situaciones.
#Para consulta o guardar datos.
#a adicionar Añadir elemento a un fichero.
#w Modo de escritura de ficheros
#r modo de lectura de ficheros

#Agregar informacion nueva en un fichero
nombre = input('Nombre :')
#+ adicionar funciones extras.
#b es para adicionar binario.
#archivo = open('ejemplo.txt', 'w+')
#archivo.write(nombre)
#archivo.close()

#Cuando ya se tenga informacion en un archivo dejaremos asi para que se vaya adicionando informacion al fichero:
archivo = open('ejemplo.txt', 'a+')
archivo.write(nombre + '\n') #Para espaciar salto de linea '\n'
archivo.close()

#Metodo de lectura de ficheros o archivos
#archivo = open('ejemplo.txt','r' )
#linea = archivo.readline()
#print(archivo.read())

#Recorrer elemento por elemento para saber si existe un dato.
#for linea in archivo.readlines():
    #print(linea)

#Traer datos de fichero sin espacios en blanco por enmedio.
archivo = open('ejemplo.txt','r' )
linea = archivo.readline()
while linea != '':
    linea = archivo.readline()
    print(linea)
archivo.close()
