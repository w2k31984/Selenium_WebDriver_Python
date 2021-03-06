from selenium import webdriver
import time
import configparser


def main():
    configuracion = configparser.ConfigParser()
    configuracion.read('../Selenium_WebDriver/config.ini')
    configuracion.sections()

    webdri = configuracion['General']['chrome']
    web = configuracion['Paginas']['pagina1']

    driver = webdriver.Chrome(executable_path='../Selenium_WebDriver/chromedriver.exe')
    driver.get(web)
    time.sleep(2)
    #Realizar funciones de JS para mostrar mensaje en el navegador.
    driver.execute_script('alert("Hola usted esta recibiendo este mensaje desde python")')
    input()
    driver.quit()

if __name__ == '__main__':
    main()