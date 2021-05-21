import time
import configparser
from selenium import webdriver

def main():
    configuracion = configparser.ConfigParser()
    configuracion.read('../Selenium_WebDriver/config.ini')
    configuracion.sections()

    webdri = configuracion['General']['chrome']
    web = configuracion['Paginas']['pagina1']

    driver = webdriver.Chrome(executable_path=webdri)
    driver.get(web)
    time.sleep(2)

    #Realizar funciones de JS para navegador
    driver.execute_script('alert("Hola usted esta recibiendo este mensaje desde python")')

    input()
if __name__ == '__name__':
    main()