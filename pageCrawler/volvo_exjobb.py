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

browser.get("https://xjobs.brassring.com/TGWebHost/searchresults.aspx?partnerid=25079&siteid=5171&Codes=Volvo&AgentID=9780452&Function=runquery")

COMPANY = "Volvo Group"
#element = browser.find_element_by_xpath("""//*[@id="top"]/div/div[2]/div[5]/div[4]/p[2]/a/strong""")
#browser.execute_script("return arguments[0].scrollIntoView();", element)

time.sleep(0.3)
table = browser.find_element_by_id('idSearchresults')
table_rows = table.find_elements_by_tag_name('tr')


for row in table_rows:
    row.text
    if 'thesis' in row.text.lower():
        
        title = row.find_element_by_tag_name('a')
        location = row.find_element_by_xpath('./td[2]')
        if 'sweden' in location.text.lower():
            continue
        date = row.find_element_by_xpath('./td[3]')
        link = title.get_attribute('href')

        print('Title: {}\nDate: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, date.text, location.text, link))
#        list_of_thesis.append(dict(title= title.text, location = location.text, link=title.get_attribute('href')))


