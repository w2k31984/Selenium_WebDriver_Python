#Importando un archivo teniendo acceso a sus funciones.
#Un modulo es aquel capaz de reutilizar funciones.
#import Funciones_Modulos
#Es buena practica en los paquetes dentro de la carpeta crear un archivo __init__.py pues indica a python que es un paquete.
#from Matematicas import Funciones_Matematica
#Otra forma de llamar el paquete seria
from Matematicas.Funciones_Matematica import suma,resta,multiplicacion,division
#Funciones para modulo.
#Funciones_Modulos.suma(num1= 7, num2=20)
#Funciones_Modulos.resta(num1= 27, num2=20)
#Funciones_Modulos.multiplicacion(num1= 9, num2=3)
#Funciones_Modulos.division(num1= 9, num2=3)


#Funciones para paquetes LLamar el nombre del modulo dentro de carpeta o paquete.
#Funciones_Matematica.suma(num1= 7, num2=20)
#Funciones_Matematica.resta(num1= 27, num2=20)
#Funciones_Matematica.multiplicacion(num1= 9, num2=3)
#Funciones_Matematica.division(num1= 9, num2=3)

#Solo llamando la funcion
suma(num1= 7, num2=20)
resta(num1= 27, num2=20)
multiplicacion(num1= 9, num2=3)
division(num1= 9, num2=3)