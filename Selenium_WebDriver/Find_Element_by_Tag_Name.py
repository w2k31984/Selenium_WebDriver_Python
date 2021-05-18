import time
from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get('https://www.google.com/') #Buscaremos tags o etiquetas html que especifiquemos este solo dara la primera que ecuentre.
    time.sleep(3)
    links = driver.find_element_by_tag_name('a')
    print(links.text)
    input()


if __name__ == '__main__':
    main()