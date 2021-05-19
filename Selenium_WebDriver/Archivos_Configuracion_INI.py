#Asi es como podremos escribir en ficheros la informacion recopilada por medio de python. (PARTE I)
#Los archivos de configuracion INI guardar la configuracion de ciertas variables.
#Que se utilizan de modo continua y de manera correcta.
import configparser #Libreria encargada de escribir los archivos .INI

configuracion = configparser.ConfigParser()
configuracion['General'] = {'chrome':'chromedriver.exe'}
configuracion['Paginas'] = {'pagina1':'https://www.google.com/','pagina2':'https://www.w3schools.com/'}

#Creando archivo
archivo = open('config.ini','w+')
configuracion.write(archivo)

