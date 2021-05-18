import time
from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get('https://www.w3schools.com/html/default.asp')
    time.sleep(3)
    driver.find_element_by_partial_link_text('HTML Global Attributes').click() #Es el texto que hace el link hacia una url del sitio.
    input()

if __name__ == '__main__':
    main()