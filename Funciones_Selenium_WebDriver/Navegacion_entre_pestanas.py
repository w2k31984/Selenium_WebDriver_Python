#Uso en aplicaciones complejas que al momento de dar click a un boton nos envia a otra pestaña
#Para eso es que podemos utilizar la navegacion entre pestañas
#1a. direccion https://www.google.com/intl/es/gmail/about/
import time
import configparser
from selenium import webdriver

def main():
    configuracion = configparser.ConfigParser()
    configuracion.read('../Selenium_WebDriver/config.ini')
    configuracion.sections()

    webdri = configuracion['General']['chrome']
    web = configuracion['Paginas']['pagina3']

    driver = webdriver.Chrome(executable_path='../Selenium_WebDriver/chromedriver.exe')
    driver.get(web)

    new_tab = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/ul[1]/li[3]/a')
    new_tab.click()

    #Obteniendo ventana actual.
    paginaactual = driver.current_window_handle #Obtendremos la pagina actual en la que nos encontremos
    ventanas = driver.window_handles #Todas las pestañas o ventanas activas o abiertas.


    for v in ventanas: #Recorremos cada pestaña
        print('Estoy cambiando de Ventanas')
        time.sleep(2)

    #Cambiarnos entre las ventanas activas
    driver.switch_to.window(v)
    input()

if __name__ == '__main__':
    main()