import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get('https://www.google.com')

if __name__ == '__main__':
    main()

time.sleep(5)