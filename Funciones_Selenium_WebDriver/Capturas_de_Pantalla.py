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
    time.sleep(3)
    driver.get_screenshot_as_file('captura.png')
    driver.stop_client()
    driver.quit()

if __name__ == '__main__':
    main()