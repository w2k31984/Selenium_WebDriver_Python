#El navegador estara corriendo en segundo plano y lo monitoriaremos con el monitor de tareas
import configparser
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Agregando argumentos de trabajo
options = Options()
options.add_argument('--headless') #Con esta linea abrimos el navegador en 2o Plano palabra reservada headless

def main():
    configuracion = configparser.ConfigParser()
    configuracion.read('../Selenium_WebDriver/config.ini')
    configuracion.sections()

    webdri = configuracion['General']['chrome']
    web = configuracion['Paginas']['pagina3']

    driver = webdriver.Chrome(executable_path='../Selenium_WebDriver/chromedriver.exe',chrome_options=options)
    driver.get(web)

    #saber si estamos en la web nos permite traer el titulo de la pagina actual.
    print(driver.title)

    input()

if __name__  == '__main__':
    main()