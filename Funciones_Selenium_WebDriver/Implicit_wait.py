#Paginas con Ajax cargando recursos de manera dinamica sin recargar pagina.
#Implicit wait ya viene incluido en webdriver y se encarga de definir un tiempo de espera y es un intervalo, entra a la pagina y espera 5seg. para cargar componentes
#El tiempo de espera es equivalente a la funcion time.
import configparser
from selenium import webdriver

def main():
    configuracion = configparser.ConfigParser()
    configuracion.read('../Selenium_WebDriver/config.ini')
    configuracion.sections()

    webdri = configuracion['General']['chrome']
    web = configuracion['Paginas']['Pagina2']

    driver = webdriver.Chrome(executable_path='../Selenium_WebDriver/chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get(web)

    input()



if __name__ == '__main__':
    main()