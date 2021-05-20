#Sirve para saber si un elemento dentro del aplicativo web se encuentra habilitado o deshabilitado.
import configparser
import time
from selenium import webdriver

def main():
    configuracion = configparser.ConfigParser()
    configuracion.read('../Selenium_WebDriver/config.ini')
    configuracion.sections()

    webdri = configuracion['General']['chrome']
    web = configuracion['Paginas']['pagina1']

    driver = webdriver.Chrome(executable_path='../Selenium_WebDriver/chromedriver.exe')
    driver.get(web)

    #Buscamos por nombre el elemento
    element = driver.find_element_by_name('btnK')

    #Ver si un elemento esta visible en el sitio.
    print(element.is_displayed())

    #Ver si un elemento esta habilitado o deshabilitado.
    print(element.is_enabled())

if __name__ == '__main__':
    main()