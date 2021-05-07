#Manejo de excepciones en python con ejemplo.
num1 = (int(input('Ingrese un un numero: ')))
num2 = (int(input('Ingrese un un numero: ')))

try: #Le decimos a python que intente correr las lineas de codigo que contiene.
  division =  num1/num2 #1/0
  print(division)
#except:
    #print('Ocurrio un error')

#Mostrando el error que genera.
except ZeroDivisionError:
    print('Ocurrio un error en dividir un numero entre Zero')

#Especificar errores en ejecucion.
finally:
    print('Pudo o no ocurrir un error')

