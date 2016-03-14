from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

import json_append

PATH = os.environ["PATH"].split(':',1)[0]

chromedriver = PATH + "/chromedriver" #change to local chromedriver location
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get("http://jobs.astrazeneca.com")


#element = browser.find_element_by_xpath("""//*[@id="top"]/div/div[2]/div[5]/div[4]/p[2]/a/strong""")
#browser.execute_script("return arguments[0].scrollIntoView();", element)


browser.find_element_by_id("316").click() #sweden
time.sleep(1)
browser.find_element_by_id("1257").click() #student opportunities
time.sleep(1)
browser.find_element_by_class_name('submit').click()

job_list = browser.find_elements_by_class_name('job-res-description')
list_of_thesis = []

for l in job_list:
    
    title = l.find_element_by_class_name('job-title')
    if 'diploma' in title.text.lower():
        location = l.find_element_by_class_name('locations')
        print('Title: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, location.text, title.get_attribute('href')))

        list_of_thesis.append(dict(title= title.text, location = location.text, link=title.get_attribute('href')))


if list_of_thesis:
    json_append.update_json(list_of_thesis)