#Importando para el tiempo de nuestro aplicativo en carga
import time
#LLamando nuestro package selenium webdriver en python
from selenium import webdriver

#Ordenando nuestro codigo en funciones.
def main():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
#Abriendo nuestra primera pagina web.
    driver.get('https://www.google.com')
    input()

if __name__ == "__main__":
    main()

time.sleep(5)
