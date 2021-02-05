"""
Crie um programa com selenium que

* Jogue o jogo
* Quando você ganhar o script deve parar de ser executado
"""
from selenium import webdriver
from time import sleep

#Google Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=r'C:\Program Files\chromedriver_v88.0.4324.96\chromedriver.exe')
browser.get("https://curso-python-selenium.netlify.app/exercicio_02.html")

sleep(1.5)

a = browser.find_element_by_tag_name('a')
p = browser.find_elements_by_tag_name('p')

numero_esperado = int((p[1].text).split(' ')[-1])

while True:
    a.click()
    p = browser.find_elements_by_tag_name('p')
    if p[-1].text == f"Você ganhou: {numero_esperado}":
        break
