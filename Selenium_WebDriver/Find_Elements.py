import time
from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get('https://www.w3schools.com/')
    time.sleep(1)
    links = driver.find_elements_by_tag_name('a')

    #Recorriendo la lista por el bucle for
    for l in links:
        print(l.text + ': ' + l.get_attribute('href')) #Nos da los parametros hacia que URL esta apuntando.


if __name__ == '__main__':
    main()
time.sleep(2)
