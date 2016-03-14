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

PATH = os.environ["PATH"].split(':',1)[0]

chromedriver = PATH + "/chromedriver" #change to local chromedriver location
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get("https://jobs.bombardier.com/key/final-thesis-bombardier-jobs.html")

COMPANY = "Bombardier"

table = browser.find_element_by_id('searchresults')
#print(table.get_attribute('innerHTML'))
table_rows = table.find_elements_by_tag_name('tr')[2:]


for row in table_rows:
    if 'thesis' in row.text.lower():
        location = row.find_element_by_xpath('./td[2]')

        if 'SE' not in location.text:
            continue

        title = row.find_element_by_tag_name('a')
        date = row.find_element_by_xpath('./td[3]')
        link = title.get_attribute('href')


        print('Title: {}\nDate: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, date.text, location.text, link))
#        list_of_thesis.append(dict(title= title.text, location = location.text, link=title.get_attribute('href')))


