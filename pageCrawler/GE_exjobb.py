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

browser.get("http://jobs.gecareers.com/search?q=thesis")

COMPANY = "General Electric"

table = browser.find_element_by_id('searchresults')
table_rows = table.find_elements_by_tag_name('tr')[2:]


for row in table_rows:
    
    if 'thesis' in row.text.lower() and 'sweden' in row.text.lower():

        title = row.find_element_by_tag_name('a')
        location = row.find_element_by_xpath('./td[2]')
        date = row.find_element_by_xpath('./td[3]')
        link = title.get_attribute('href')

        print('Title: {}\nDate: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, date.text, location.text, link))
#        list_of_thesis.append(dict(title= title.text, location = location.text, link=title.get_attribute('href')))


