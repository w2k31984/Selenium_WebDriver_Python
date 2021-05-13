import time
from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get('https://www.w3schools.com/html/')
    time.sleep(3)
    driver.find_element_by_class_name('bigbtn').click() # Objeto de HTML References (HTML Elements : https://www.w3schools.com/tags/default.asp)
    #driver.find_element_by_id('w3loginbtn').click()
    time.sleep(3)


if __name__== '__main__':
    main()

time.sleep(3)