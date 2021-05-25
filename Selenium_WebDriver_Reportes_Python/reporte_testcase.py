#Creando reporte de test con HTMLTestRunner http://tungwaiyip.info/software/HTMLTestRunner.html
import unittest
import time
import HtmlTestRunner
from selenium import webdriver

class MyTestSuite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='../Selenium_WebDriver/chromedriver.exe')

    def test_get_title(self):
        driver = self.driver
        try:
            driver.get('https://www.ui5cn.com/')
        except Exception as ex:
            print(ex)
        else:
            time.sleep(2)
            my_title = 'UI5CN'
            self.assertEqual(driver.title, my_title, 'Not Matching')
    def tearDown(self):
           self.driver.stop_client()
           self.driver.quit()


if __name__ == '__main__':
#Para generar el reporte en html debe correrse el archivo que ejecuta la prueba desde cmd con python reporte_testcase.py
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\cristian_parada\Desktop\Selenium WebDriver Python\Selenium_WebDriver_Reportes_Python'))