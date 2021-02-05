from selenium import webdriver
from time import sleep

def find_by_text(browser, tag, text):
    elementos = browser.find_elements_by_tag_name(tag)
    for elemento in elementos:
        if elemento.text == text:
            return elemento

def find_by_href(browser, link):
    elementos = browser.find_elements_by_tag_name('a')
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento

#Google Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=r'C:\Program Files\chromedriver_v88.0.4324.96\chromedriver.exe')
browser.get("http://selenium.dunossauro.live/aula_04_a.html")

sleep(1.5)

# elemento_google = find_by_text(browser, 'a', 'Google')

elemento_google = find_by_href(browser, 'google')
