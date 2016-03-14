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

import json_append

PATH = os.environ["PATH"].split(':',1)[0]

chromedriver = PATH + "/chromedriver" #change to local chromedriver location
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get("https://boliden.csod.com/ats/careersite/search.aspx?site=5&c=boliden")
baseurl = "https://boliden.csod.com/ats/careersite/JobDetails.aspx?id="

#job_list = browser.find_elements_by_tag_name('''li''')
job_list = browser.find_elements_by_xpath('''//ul/li''')

list_of_thesis = []

for l in job_list:
    try:
        title = l.find_element_by_tag_name('a')
        location_data = l.find_element_by_class_name("FieldValue").text
        
    except:
        continue
    department, location = re.findall('\((.*?)\|(.*?)\)', location_data)[0]
    
    link_info = title.get_attribute('href')
    match = re.findall('.*?id=([^"]*)', link_info)
    

    print('Title: {}\nDepartment: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, department, location, baseurl+match[0]))
    list_of_thesis.append(dict(title= title.text, location = location, link=baseurl+match[0]))

    browser.quit()

if list_of_thesis:
    json_append.update_json(list_of_thesis)
