#Xpath es la forma de certeza que vamos acertar en el elemento correspondiente
#Este funciona con ruta absoluta o mas larga desde directorio raiz hacia el fichero.
#Es la manera mas precisa y sencilla para buscar elementos.
import time
from selenium import webdriver

def  main():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get('https://www.google.com/')
    time.sleep(2)
    texto = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/a[1]').text
    print(texto)
    input()

if __name__ == '__main__':
    main()