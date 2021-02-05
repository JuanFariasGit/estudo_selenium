from selenium import webdriver
from time import sleep

#Google Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=r'C:\Program Files\chromedriver_v88.0.4324.96\chromedriver.exe')
browser.get("http://selenium.dunossauro.live/aula_04_a.html")

sleep(1.5)

ul = browser.find_element_by_tag_name('ul')
p = ul.find_elements_by_tag_name('li')
p[0].find_element_by_tag_name('a')
