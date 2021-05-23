#Utilizar selenium WebDriver desde Navegador Brave.
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
#Ejecuta la ruta para el navegador
options.binary_location = r'ruta_instalado_brave\brave.exe'

def main():
    driver = webdriver.Chrome(executable_path='chromedriver.exe',options = options)
    driver.get('https://www.google.com/')
    input()

if __name__ == '__main__':
    main()
