from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os


chromedriver = "/Users/fredrikjacobson/Desktop/code/chromedriver" #change to local chromedriver location
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get("http://www.volvocars.com/intl/about/our-company/careers/job-search")

job_list = browser.find_elements_by_xpath("""//*[@id="volvo"]/div[3]/div/div""")

for i in range(1, len(job_list)-1): #1 to skip labels and len() -1 to skip last row "we are sorry..."
    position = job_list[i].find_element_by_tag_name('dt')
    
    #Test if thesis work
    if 'thesis' in position.text.lower():
        location, app_date = job_list[i].find_elements_by_tag_name('dd')
        link_description = job_list[i].find_element_by_css_selector('a').get_attribute('href')

        print(' Position: {} \n Location: {} \n Last Application Date: {}'.format(position.text, location.text, app_date.text))

        browser.execute_script("window.open('');")
        browser.switch_to_window(browser.window_handles[1])
        browser.get(link_description)

        description = browser.find_element_by_class_name('cl-description').text
        print(description)

        time.sleep(1)
        browser.close()
        browser.switch_to_window(browser.window_handles[0])


        
    else:
        continue
