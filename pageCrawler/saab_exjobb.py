from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import re

from readability.readability import Document

chromedriver = "/Users/fredrikjacobson/Desktop/code/chromedriver" #change to local chromedriver location
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get("http://saabgroup.com/sv/career/job-opportunities/?&c=Sweden")

COMPANY = "SAAB"
#element = browser.find_element_by_xpath("""//*[@id="top"]/div/div[2]/div[5]/div[4]/p[2]/a/strong""")
#browser.execute_script("return arguments[0].scrollIntoView();", element)


table = browser.find_element_by_class_name('vacancies')
table_rows = table.find_elements_by_tag_name('li')

for row in table_rows:
    if 'examen' in row.text.lower():
        print(row.text)
        title = find_element_by_class_name('title')
        location = find_elements_by_tag_name('location')
        date = find_element_by_class_name('date')
        link = title.get_attribute('href')


#        list_of_thesis.append(dict(title= title.text, location = location.text, link=title.get_attribute('href')))


