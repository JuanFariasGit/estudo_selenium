from selenium import webdriver
from time import sleep

#Google Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path=r'C:\Program Files\chromedriver_v88.0.4324.96\chromedriver.exe')
browser.get("https://curso-python-selenium.netlify.app/aula_03.html")

sleep(1)

a = browser.find_element_by_tag_name('a')
p = browser.find_element_by_tag_name('p')

for click in range(1, 11):
    a.click()
