#Configuracion para trabajar con Egde navegador de microsoft
#Debemos ver la version del navegador siempre

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    driver = webdriver.Edge(executable_path='msedgedriver.exe')
    driver.get('https://www.google.com')
    driver.execute_script("alert('Ejecucion Terminada con Exito')")
    time.sleep(3)
    driver.stop_client()
    driver.quit()

if __name__ == '__main__':
    main()

