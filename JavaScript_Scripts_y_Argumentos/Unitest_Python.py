#Realizacion de pruebas unitarias .
#Unitest buscara todas las palabras llamadas test.
import time
import configparser
import unittest
from selenium import webdriver

#Trabajaremos con una clase que es hija que hereda la funcionalidad de clase padre.
class MyTest(unittest.TestCase):
    def test_web(self):
        configuracion = configparser.ConfigParser()
        configuracion.read('../Selenium_WebDriver/config.ini')
        configuracion.sections()

        webdri = configuracion['General']['chrome']
        web = configuracion['Paginas']['pagina1']

        driver = webdriver.Chrome('../Selenium_WebDriver/chromedriver.exe')
        driver.get(web)
        driver.execute_script('prompt("Introduce tu nombre: ", "Cristian SkinWalker")')
        alerta = driver.switch_to_alert()
        time.sleep(2)
        alerta.accept()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()

