import random
import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By

class myTestWeb(unittest.TestCase):
    def testWeb(self):
        self.driver = webdriver.Chrome(executable_path='../Selenium_WebDriver/chromedriver.exe')
        self.driver.get('https://www.booking.com/index.es.en')
        time.sleep(3)
       #Entrando a seleccinar idioma
        self.driver.find_element_by_xpath('/html/body/header/nav[1]/div[2]/div[2]/button/span/div/img').click()
        time.sleep(2)
        #Seleccionando idioma Ingles
        self.driver.find_element_by_xpath('//*[@id="language-selection"]/div/div/div/div/div/div[1]/div/div[2]/div/ul/div[1]/ul/li[2]/a/div/div[2]').click()
        time.sleep(2)
        buscar = self.driver.find_element(By.NAME, "ss")
        buscar.send_keys('Gran Palas Hotel-Spa Incluido')
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[3]/div/form/div[3]/div[2]/button').click()
        time.sleep(3)
        #Buscando elementos de hoteles debe traer todos los enlaces
        elementos = self.driver.find_elements_by_tag_name('a')
        #Haciendo verificacion Nome es equivalente a vacia o sin elementos.
        if elementos != None:
           hotelramdom = []
           #for  l in elementos:
                 #print(l.get_attribute('href'))
        #Utilizando tecnica list completions se especifica para tener un bucle con lo que queremos.
           hotel = [l for l in elementos if 'hotels/detail' in str(l.get_attribute('href'))]
        #Añadiendo elementos
           #for h in hotel:
               #hotelramdom.append(h.get_attribute('href'))
           #self.driver.execute_script(f'window.open("{random.choice(hotelramdom)}")')
           #input()
        else:
            self.driver.stop_client()
            self.driver.quit()

if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\cristian_parada\Desktop\Selenium WebDriver Python\Selenium_WebDriver_Reportes_Python'))

