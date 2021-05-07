#Ejemplo de funciones y manejo de errores
#Existen dos tipos de funciones con argumento o sin argumento
#Las con argumentos
def suma(num1, num2):
    print(num1+num2)
def resta(num1, num2):
    print(num1-num2)
def multiplicacion(num1, num2):
    print(num1*num2)
def division(num1, num2):
    print(num1/num2)

def menu():
  while True:
    print('''
    Calculadora Sencilla
    1 Sumar.
    2 Restar.
    3 Multiplicar.
    4 Dividir.
    ''')
    try:
        opcion = int(input('Introduzca la opcion que quiere realizar : '))
        if opcion == '':
           print('Introduzca un valor valido')
        elif opcion == 1:
           num1 = int(input('Ingresa un numero: '))
           num2 = int(input('Ingrese otro numero: '))
           suma(num1,num2)
        elif opcion == 2:
            num1 = int(input('Ingresa un numero: '))
            num2 = int(input('Ingrese otro numero: '))
            resta(num1, num2)
        elif opcion == 3:
            num1 = int(input('Ingresa un numero: '))
            num2 = int(input('Ingrese otro numero: '))
            multiplicacion(num1= num1, num2=num2)
        elif opcion == 4:
            num1 = int(input('Ingresa un numero: '))
            num2 = int(input('Ingrese otro numero: '))
            division(num1= num1, num2= num2)
        else:
          print('Opcion ingresada es invalida')
    except ValueError:
          print('Opcion ingresada es invalida')
#print(opcion)
#Llamada a la funcion para que se ejecute.
menu()
