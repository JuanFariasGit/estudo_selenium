from selenium import webdriver
from time import sleep
from pprint import pprint

def get_links(browser, tag):
    elemento = browser.find_element_by_tag_name(tag)
    ancoras = elemento.find_elements_by_tag_name('a')

    links = {}

    for ancora in ancoras:
        links[ancora.text] = ancora.get_attribute('href')

    return links

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=r'C:\Program Files\chromedriver_v88.0.4324.96\chromedriver.exe')
browser.get("http://selenium.dunossauro.live/aula_04.html")

sleep(1.5)

links = get_links(browser, 'main')

pprint(links)
