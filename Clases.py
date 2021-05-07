#Las clases pertenecen a POO veremos como se maneja en Python este paradigma de programacion
#Trata de acercar la programacion a caracteristicas del mundo fisico.
#Ejemplo de coche y dotarlo de los objetos necesarios que lo componen.
#Las funciones son iguales que los metodos.
#Los objetos declarados en una variable son instancias y se llama instancia de objetos.
class Coche:
    def __init__(self, color, gasolina, avanzar): #Manera obligatoria es la inicializadora del objeto.
        self.color = color
        self.gasolina = gasolina
        self.avanzar = avanzar
#Funciones dentro de objeto Coche
    def Gasolina(self):
        if self.gasolina > 1:
            print('El tanque posee Gasolina')
        else:
            print('El tanque esta vacio debe recargar Gasolina')

    def Avanzar(self):
        if self.gasolina >1 and self.avanzar== True:
            print('Coche en Marcha')
        elif self.gasolina >1 and self.avanzar== False:
            print('Coche no esta en Marcha sino en Retroceso')
        else:
            print('Coche sin Gasolina o estacionado')
#Instanciando el objeto en una variable
coche = Coche(color='Maximum Steel',gasolina=10,avanzar=True)
print('El Color del coche es: '+coche.color)
coche.Gasolina()
coche.Avanzar()

#Reutilizando objeto.
coche1 = Coche(color='Apple Green',gasolina=0,avanzar=False)
print('El Color del coche es: '+coche1.color)
coche1.Gasolina()
coche1.Avanzar()
