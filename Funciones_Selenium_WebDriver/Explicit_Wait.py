#Funciona similar al implicit_Wait con la condicion que el WebDriver va esperar abrir la web de manera simultanea un
#intervalo en segundos, hace una llamada cada 500 milisegundos para saber si encuentra el elemento que buscamos.
#Es como una condicion que debe cumplirse antes de interactuar y esto es con componentes dinamicos que controla.
import configparser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions #Verifica si nuestro elemento se encuentra en la web
from selenium.webdriver.common.by import By

def main():
    configuracion = configparser.ConfigParser()
    configuracion.read('../Selenium_WebDriver/config.ini')
    configuracion.sections()

    webdri = configuracion['General']['chrome']
    web = configuracion['Paginas']['pagina1']

    driver = webdriver.Chrome(executable_path='../Selenium_WebDriver/chromedriver.exe')
    driver.get(web)

    #Cuando Selenium no encuentra un elemento pasa a una excepcion
    try:
        element = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.NAME, 'q'))) #Dos parametros 1)Donse se esta ejecutando la aplicacion (driver)/Until que elemento queremos encontrar
        print('Se encontro el elemento')
    #finally:
    #Podemos utilizar except tambien
    except:
        driver.quit()

if __name__ == '__main__':
    main()