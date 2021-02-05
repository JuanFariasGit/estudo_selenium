from selenium import webdriver
from urllib.parse import urlparse
from time import sleep

#Google Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=r'C:\Program Files\chromedriver_v88.0.4324.96\chromedriver.exe')
browser.get("http://selenium.dunossauro.live/aula_04_b.html")

analizar_url = urlparse(browser.current_url)
