"""
Crie um programa com selenium que gere um dicionário, onde a chave é a tag h1.

* O valor deve ser um novo dicionário
* Cada chave do valor deverá ser o valor de 'atributo'
* Cada valor deve ser o texto contido no elemento
"""
from selenium import webdriver
from time import sleep

#Google Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=r'C:\Program Files\chromedriver_v88.0.4324.96\chromedriver.exe')
browser.get("https://curso-python-selenium.netlify.app/exercicio_01.html")

sleep(1)

h1 = browser.find_element_by_tag_name('h1')
p = browser.find_elements_by_tag_name('p')

print({'H1':{'texto1':p[0].text, 'texto2':p[1].text, 'text3':p[2].text}})

browser.quit()
