from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

PATH = os.environ["PATH"].split(':',1)[0]

chromedriver = PATH + "/chromedriver" #change to local chromedriver location
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get("http://saabgroup.com/sv/career/job-opportunities/?&c=Sweden")

COMPANY = "Sandvik"

table = browser.find_element_by_tag_name('tbody')
table_rows = table.find_element_by_tag_name('tr')

for row in table_rows:
    title = row.find_element_by_xpath('./td[1]')
    subject = row.find_element_by_xpath('./td[2]')
    location = row.find_element_by_xpath('./td[3]')
    date = row.find_element_by_xpath('./td[4]')
    link = 'how to fetch link'