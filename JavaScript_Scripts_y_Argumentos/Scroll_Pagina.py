import time
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Para enviar un enter

def main():
    configuracion = configparser.ConfigParser()
    configuracion.read('../Selenium_WebDriver/config.ini')
    configuracion.sections()

    webdri = configuracion['General']['chrome']
    web = configuracion['Paginas']['pagina1']

    driver = webdriver.Chrome('../Selenium_WebDriver/chromedriver.exe')
    driver.get(web)
    time.sleep(2)

    buscar = driver.find_element_by_name('q')
    time.sleep(2)

    #Realizar una busqueda
    buscar.send_keys('Hacking con Python', Keys.ENTER)
    time.sleep(2)

    #Realizar scroll hasta el final de la pagina
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    input()


if __name__ == '__main__':
    main()