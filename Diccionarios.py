#Ultimo conjunto de datos de Python
#Esta definido con llaves
a = {'persona':'Cristian Parada','fruta':'Guineo','color':'Azul','edad':20, 'fecha nacimiento':'08/09/84'}
#for i in a:
#    print(a[i])
# La funcion para poder hacer un contenido de un diccionario es dict
b = dict(nombre='Cristian Menendez', color='negro',fruta='Mango',ciudad='Berlin',telefono=77687265)
print(b)

# La funcion zip convierte un numero de elementos en un diccionario
c = zip('Hola', 'Iglesia',[3.141615, 5])
print(c)

#Ver metodos que tiene un diccionario
print(dir(c))

print(dir(b))
print(b.values())
#Actualizar  un nuevo dato en  diccionario
b.update(edad=20)
print(b)

#Valor de un objeto de diccionario
print(b.get('nombre'))
print(b.get('telefono'))
