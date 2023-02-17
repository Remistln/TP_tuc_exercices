from selenium import webdriver
from selenium.webdriver. common.by import By
import time
import random

def return_title_site():
    driver = webdriver.Chrome()
    driver.get("https://www.twitter.com/")
    driver.find_element(by=By.PARTIAL_LINK_TEXT, value="S'inscrire").click()
    title = driver.title
    print(title)
    driver.close()
    return title

# def return_title_wikiroulette():
#     driver = webdriver.Chrome()
#     driver.get("https://www.wikiroulette.co/")
#     driver.implicitly_wait(3)
#     title = driver.find_element(by=By.CLASS_NAME, value="mw-page-title-main")
#     # span = driver.find_elements(by=By.TAG_NAME, value='span')
#     # print([x.get_attribute('class') for x in span])
#     print(title)
#     driver.close()
#     # return title

return_title_site()