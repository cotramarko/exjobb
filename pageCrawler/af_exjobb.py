from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

PATH = os.environ["PATH"].split(':',1)[0]

chromedriver = PATH + "/chromedriver" #change to local chromedriver location
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get("http://www.afconsult.com/sv/jobba-hos-oss/lediga-jobb/")



#time.sleep(1)    #might need to explicitly wait for website to load

find_button = browser.find_element_by_id("""dk1-combobox""").click()
option = browser.find_element_by_id("dk1--2024534255__jobFilters").click()

time.sleep(1)
content = browser.find_element_by_id("contentItemListing_6373")
job_list = content.find_elements_by_css_selector('.block.col.regular-12')

for l in job_list:
    title = l.find_element_by_css_selector(".col.regular-6")
    if "exjobb" in title.text.lower():
        print(title.text)
        link = l.find_element_by_tag_name("a")
        location, app_date = l.find_elements_by_css_selector(".col.regular-3")

        print('Title: {}\nLocation: {}\nApplication Date: {}\n\n'.format(title.text, location.text, app_date.text, link.get_attribute('href')))

browser.quit()
