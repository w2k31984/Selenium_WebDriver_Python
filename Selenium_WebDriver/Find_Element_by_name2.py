import time
from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get('https://www.google.com/')
    time.sleep(2)
    driver.find_element_by_name('q').send_keys('selenium')
    input()

if __name__ == '__main__':
    main()