import configparser
import time
from selenium import webdriver

def main():
    configuracion = configparser.ConfigParser()
    configuracion.read('../Selenium_WebDriver/config.ini')
    configuracion.sections()

    webdri = configuracion['General']['chrome']
    web = configuracion['Paginas']['pagina3']

    driver = webdriver.Chrome(executable_path='../Selenium_WebDriver/chromedriver.exe')
    driver.get(web)
    time.sleep(5)

    print('Estoy saliendo del programa')

    #Deteniendo el programa de manera correcta
    driver.stop_client()
    #Saliendo del programa
    driver.quit()

if __name__ == '__main__':
    main()