import time
from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get('https://www.w3schools.com/')
    #input()
    time.sleep(5)
    driver.find_element_by_css_selector('#w3loginbtn').click() #Conseguiremos copiando del objeto el selector del objeto.
    input()
if __name__ == '__main__':
    main()

#time.sleep(3)