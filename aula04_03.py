from selenium import webdriver
from time import sleep

def find_by_text(browser, tag, text):
    elementos = browser.find_elements_by_tag_name(tag)
    for elemento in elementos:
        if elemento.text == text:
            return elemento

#Google Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=r'C:\Program Files\chromedriver_v88.0.4324.96\chromedriver.exe')
browser.get("http://selenium.dunossauro.live/aula_04_b.html")

sleep(1.5)

nomes_das_caixas = ['um', 'dois', 'tres', 'quatro']

for nome in nomes_das_caixas:
    find_by_text(browser, 'div', nome).click()

for nome in nomes_das_caixas:
    sleep(0.3)
    browser.back()

for nome in nomes_das_caixas:
    sleep(0.3)
    browser.forward()
