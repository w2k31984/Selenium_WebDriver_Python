import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get('https://www.google.com')
    time.sleep(3)
    buscar = driver.find_element(By.NAME, 'q')
    buscar.send_keys('Python', Keys.ENTER)
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/a').click()
    time.sleep(5)
    input()
if __name__== '__main__':
    main()
