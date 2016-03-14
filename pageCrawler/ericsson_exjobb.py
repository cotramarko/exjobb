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

browser.get("https://jobs.ericsson.com/search/?q=&locationsearch=sweden")

COMPANY = "Ericsson"

if int(browser.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div/span/span[1]/b[2]""").text) > 25:
    second_page = True
list_of_thesis = []

table_rows = browser.find_elements_by_css_selector('tr.data-row.clickable')

for _ in range(2):

    for row in table_rows:

        if 'thesis' in row.text.lower():
            title = row.find_element_by_tag_name('a')
            location = row.find_element_by_xpath('./td[2]')
            date = row.find_element_by_xpath('./td[3]')
            link = title.get_attribute('href')

            print('Title: {}\nDate: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, date.text, location.text, link))

    if second_page:
        browser.find_element_by_class_name('paginationItemLast').click()
        table_rows = browser.find_elements_by_css_selector('tr.data-row.clickable')
    else:
        break



#        list_of_thesis.append(dict(title= title.text, location = location.text, link=title.get_attribute('href')))


