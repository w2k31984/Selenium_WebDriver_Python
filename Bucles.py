#Bucles o ciclos se relacionan a la manera de recorrer un conjunto de datos de manera iterativa.
#Funciona mucho para tareas automatizadas.
#En python solo existe el While y el For.
#Bucle for

a = {'persona':'Cristian Parada','fruta':'Guineo','color':'Azul','edad':20, 'fecha nacimiento':'08/09/84','telefono': 77687265}

# i variable iterativa
#for i in a:
    #print(i)
#Funcion Range genera un rango de numeros

#for i in range(0,101):
    #print(i)
#for i in range(0,len(a)):
#  print(a[i])

#Consulta con una lista
b = list(range(0,100))
for i in b:
    print(i)
#print(b)

#Lista que nos traiga numeros de 3 en 3
b = list(range(0,100,3))
for i in b:
    print(i)

#Sentencia While (Mientras) No imprime mientras no se cumpla una condicion
print('Ejemplo while')
i = 0
while i < 10 : #esta condicion abriria por si sola un bucle infinito.
    print(i)
    i = i+1

#Recorrer una lista con while
while i < len(b):
    print(b[i])
    i= i+1

#



