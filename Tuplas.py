#Las tuplas son tipos de datos son tres listas, tuplas y diccionarios.
#Son similares a las listas y comparten metodos con las listas son inmutables
# #una vez definimos un valor no puede ser alterado
#tuple o ()
a = (20,23.21,'Hola','Avion', True)
print(a)
#print(type(a))

#Ver metodos para las tuplas
#print(dir(a))

#Contar el # de elementos que se repite en una lista
print(a.count('Hola'))

#POdemos saber la posicion de un elemento en una tupla
print(a.index('Hola'))

#Acceder a valores de las tuplas.
print(a[3])

#Obtener todos los valores de una tupla en forma ascendente o vertical.
for i in a:
    print(i)




