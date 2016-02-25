from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

import json_append

chromedriver = "/Users/fredrikjacobson/Desktop/code/chromedriver" #change to local chromedriver location
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get("http://www.billerudkorsnas.com/sv/Karriar/Lediga-jobb/Exjobb2/")


job_list = browser.find_elements_by_xpath('''//*[@id="primarycontent"]/article/table/tbody/tr''')
list_of_thesis = []
for l in job_list:
    
    title = l.find_element_by_class_name('listTitle')
    location = l.find_element_by_xpath('''.//td[2]''')
    link = l.find_element_by_tag_name('a')
    
    print('Title: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, location.text, link.get_attribute('href')))
    list_of_thesis.append(dict(title= title.text, location = location.text, link=link.get_attribute('href')))


browser.quit()

if list_of_thesis:
    json_append.update_json(list_of_thesis)
