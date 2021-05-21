#Generar alertas en pantalla
import time
import configparser
from selenium import webdriver

def main():
    configuracion = configparser.ConfigParser()
    configuracion.read('../Selenium_WebDriver/config.ini')
    configuracion.sections()

    webdri = configuracion['General']['chrome']
    web = configuracion['Paginas']['pagina1']

    driver = webdriver.Chrome('../Selenium_WebDriver/chromedriver.exe')
    driver.get(web)
    time.sleep(2)

    # Realizar funcion de JS para mostrar mensaje en el navegador.
    driver.execute_script('alert("De click al boton de aceptar")')
    time.sleep(2)

    #Permite que en vez que estemos en la web pasamos a la alerta
    aceptar = driver.switch_to_alert()
    time.sleep(1)

    #Dando click al boton aceptar de la alerta
    aceptar.dismiss()
    input()

    #Dar click al boton para aceptar.

if __name__ == '__main__':
    main()