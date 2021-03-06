# -*- coding: utf-8 -*-
import browserobject
import sys
import os
import time

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from json_append import *
from readability.readability import Document




browser = browserobject.start_browser("http://www.volvocars.com/intl/about/our-company/careers/job-search")
job_list = browser.find_elements_by_xpath("""//*[@id="volvo"]/div[3]/div/div""")

list_of_thesis = []
for i in range(1, len(job_list)-1): #1 to skip labels and len() -1 to skip last row "we are sorry..."
    position = job_list[i].find_element_by_tag_name('dt')
    
    #Test if thesis work
    if 'thesis' in position.text.lower():
        location, app_date = job_list[i].find_elements_by_tag_name('dd')
        link_description = job_list[i].find_element_by_css_selector('a').get_attribute('href')

        print(' Position: {} \n Location: {} \n Last Application Date: {}'.format(position.text, location.text, app_date.text))

####
        list_of_thesis.append(dict(title= position.text, location = location.text, link=link_description))
####
        browser.execute_script("window.open('');")
        browser.switch_to_window(browser.window_handles[1])
        browser.get(link_description)


        description = browser.find_element_by_class_name('cl-description').text
        body = browser.find_element_by_class_name('cl-description').get_attribute('outerHTML') #HTML to send to readability
        
        # readable_article = Document(body).summary()
        # with open('thesis' + str(i), 'w') as f:

        #     print(readable_article, file=f)
        # #print(description)

        time.sleep(1)
        browser.close()
        browser.switch_to_window(browser.window_handles[0])


        
    else:
        continue
# ###
# if list_of_thesis:
#     json_append.update_json(list_of_thesis)
# ###