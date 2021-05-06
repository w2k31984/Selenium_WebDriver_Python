#Condicionales

dato = int(input('Introduzca un dato: '))
if dato > 10:
    print('Dato numerico mayor a 10')
if dato < 10:
    print('Dato numerico menor a 10')
elif dato < 0: #elif opciones B u otras opciones siempre se debe colocar un if primero al igual que else.
    print('Dato numerico es pequeño')
else:
    print('Dato numerico exacto')