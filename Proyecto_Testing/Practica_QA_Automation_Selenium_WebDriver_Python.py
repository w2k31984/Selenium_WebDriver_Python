#Sitio de Prueba https://www.phptravels.net/home
#La prueba la realizaremos en el proceso de elegir tours.
import time
import unittest #Realizar test case de manera unitaria
import random #Seleccionar datos de manera aleatoria
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MyTestWeb(unittest.TestCase):
    def test_uno(self):
        driver = webdriver.Chrome(executable_path='../Selenium_WebDriver/chromedriver.exe')
        driver.get('https://www.phptravels.net/home')
        time.sleep(2)
    #Abriendo las opciones de idioma
        driver.find_element_by_xpath('//*[@id="dropdownLangauge"]').click()
        time.sleep(2)
    #Cambiando el idioma a español
        driver.find_element_by_id('es').click() #Seleccionando idioma español
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="search"]/div/div/div/div/div/nav/ul/li[4]/a').click() #Seleccionando opcion Tours
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[4]/div/div/form/div/div/div[1]/div/div[2]/div').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="select2-drop"]/ul/li[1]/div').click() #Lista Tours
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="select2-drop"]/ul/li[1]/ul/li[1]/div').click() #Sheraton trip
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="tourtype_chosen"]/a').click() #Seleccionando destino de tour.
        time.sleep(2)
        #Opcion aumentar personas.
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[4]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div[2]/div/span/button[1]').click()
        time.sleep(2)
        #Opcion de boton buscar.
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[4]/div/div/form/div/div/div[4]/button').click()
        #Confirmando ejecucion del test case de prueba
        driver.execute_script("alert('Ejecucion Terminada con Exito')")
        time.sleep(3)
        driver.stop_client()
        driver.quit()





if __name__  ==  '__main__':
    unittest.main()

