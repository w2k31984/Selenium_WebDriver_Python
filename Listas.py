#limite= int(input('Introduzca el limite: '))
#Listas en Python arrays o list almacenan valores de diferente tipo no son extralimitadas.
a=['Coche', 1, 'Hola', 2, 'Agua', 3,2.5,9, 'Hielo', 4.9,True, False,3.7, 43,19.5,'Cecilia','Gasolina',5.29]
#print(a)

#Longitud de una lista.
#print(len(a))

#Imprimir posicion de lista la posicion empieza en cero.
#print(a[5])

#Imprimir posiciones de lista en forma aleatoria
#print(a[0:12])

#Imprimiendo el limite colocado por el usuario entre cero y 13
#print(a[0:limite])

#Al no conocer el limite de la lista solo colocaremos cero y los dos puntos
#print(a[0:])

#Conociendo el ultimo valor de la lista
#print(a[-1])

#Reemplazar valores de la lista
#a[0] = 'Sedan'
#print(a[0])

#Añadir valores a una lista, estos se van a ir añadiendo al final de la lista.
#a.append('Amsterdam')
#a.append(3.1416)
#print(a)

#Imprimir cantidad de valores que posee una lista
#print(a.count('Amsterdam'))
#print(a.count(3.1416))
#print(a)

#Imprimir un valor adicional a lista
a.extend([3])
print(a)

#Buscar datos en una lista.
print(a.index('Hola'))
print(a[2])

#Eliminar el ultimo elemento de la lista
print(a.pop())
print(a)

#Eliminar elemento en base a uno especifico.
a.remove('Hielo')
print(a)

#Invertir valores de la lista
b= a.reverse()
print(b)

#Ordenar elementos de la lista si es que pueden ordenarse.
#a.sort()

#Concatenar elementos de lista convirtiendo en una cadena de texto
b=['ho', 'la']
print(b)
print(''.join(b))

