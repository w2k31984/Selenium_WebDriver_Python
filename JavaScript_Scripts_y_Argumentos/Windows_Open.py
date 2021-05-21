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

    #Abrir nueva ventana
    driver.execute_script('window.open("https://www.bing.com/")')
    input()
    driver.quit()

if __name__ == '__main__':
    main()