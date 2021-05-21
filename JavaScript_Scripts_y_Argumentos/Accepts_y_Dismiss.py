import time
import configparser
from selenium import webdriver

def main():
    configuracion = configparser.ConfigParser()
    configuracion.read('../Selenium_WebDriver/config.ini')
    configuracion.sections()

    webdri = configuracion['General']['chrome']
    web = configuracion['Paginas']['pagina1']

    driver = webdriver.Chrome(executable_path='../Selenium_WebDriver/chromedriver.exe')
    driver.get(web)
    driver.execute_script('prompt("Introduzca su nombre: " , "Cristian Moises Parada Mendoza")')
    alert = driver.switch_to_alert()
    time.sleep(2)
    #Aceptar
    #alert.accept()
    #rechazar
    alert.dismiss()


if __name__ == '__main__':
    main()