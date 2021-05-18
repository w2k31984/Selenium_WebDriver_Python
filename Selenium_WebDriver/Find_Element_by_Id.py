import time
from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get('https://www.w3schools.com/')
    time.sleep(2)
    driver.find_element_by_id('navbtn_references').click()
    input()

if __name__ == '__main__':
    main()
