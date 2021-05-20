#Podemos abrir el navegador que estamos utilizando en modo incognito
#Esto puede ser para no tener registros de navegacion u otras razones.
import time
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--incognito') #Palabra reservada para incognito

def main():
    configuracion = configparser.ConfigParser()
    configuracion.read('../Selenium_WebDriver/config.ini')
    configuracion.sections()

    webdri = configuracion['General']['chrome']
    web = configuracion['Paginas']['pagina3']

    driver = webdriver.Chrome(executable_path='../Selenium_WebDriver/chromedriver.exe', chrome_options=options)
    driver.get(web)
    time.sleep(3)
    #Tomando captura de modo incognito en navegador.
    driver.get_screenshot_as_file('captura1.png')

    print(driver.title)

if __name__ == '__main__':
    main()


