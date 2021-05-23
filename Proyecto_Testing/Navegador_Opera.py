#Configuracion para navegador Opera de WebDriver
#sitio https://github.com/operasoftware/operachromiumdriver/releases
#Dependera de la version del navegado asi sera la version de opera que descarguemos
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    driver = webdriver.Opera(executable_path='operadriver.exe')
    driver.get('https://www.google.com')
    driver.execute_script("alert('Ejecucion Terminada con Exito')")
    time.sleep(3)
    driver.stop_client()
    driver.quit()


if __name__ == '__main__':
    main()