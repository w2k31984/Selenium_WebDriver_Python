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
   driver.get('https://www.bing.com/')
   time.sleep(5)
   driver.get(web)
   time.sleep(5)

   #Volver a pagina de bing
   driver.back()

   #Volver a pagina de gmail
   driver.forward()

   input()

if __name__ == '__main__':
    main()