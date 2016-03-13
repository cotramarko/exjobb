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


chromedriver = "/Users/fredrikjacobson/Desktop/code/chromedriver" #change to local chromedriver location
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get("http://www.goteborgenergi.se/Om_oss/Karriar/Student/Examensarbete")

COMPANY = "Göteborgs Energi"
time.sleep(0.3)
table = browser.find_element_by_class_name('Dx-Content-Table')
table_rows = table.find_elements_by_tag_name('tr')[1:]


for row in table_rows:
    
    title = row.find_element_by_tag_name('a')
    location = 'Gothenburg'
    link = title.get_attribute('href')

    print('Title: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, location, link))
#        list_of_thesis.append(dict(title= title.text, location = location.text, link=title.get_attribute('href')))


