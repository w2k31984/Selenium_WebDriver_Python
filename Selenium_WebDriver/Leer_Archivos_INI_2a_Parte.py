#Leer archivos .INI
import configparser
import time
from selenium import webdriver

def main():
    configuracion = configparser.ConfigParser()
    configuracion.read('config.ini')
    configuracion.sections()      #Dividir el archivo en secciones.

    webdri = configuracion['General']['chrome']
    pagina = configuracion['Paginas']['Pagina2']

    driver = webdriver.Chrome(executable_path=webdri)
    driver.get(pagina)
    time.sleep(5)
    input()

if __name__ == '__main__':
    main()
