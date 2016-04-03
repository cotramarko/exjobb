import browserobject
import os
from selenium.common.exceptions import NoSuchElementException
import sys

#browser = browserobject.start_browser("https://skf.tms.hrdepartment.com/cgi-bin/a/searchjobs_quick.cgi?kand=thesis&country=&qty=25&sj=1&order=jobs.timedate+DESC&search=Search+Jobs")
browser = browserobject.start_browser("https://skf.tms.hrdepartment.com/cgi-bin/a/searchjobs_quick.cgi?kand=thesis&geog=custom__59&country=&qty=25&sj=1&order=jobs.timedate+DESC&search=Search+Jobs")

COMPANY = "SKF"

try:
    alert = browser.find_element_by_class_name('alert')
    print(alert.text)
    sys.exit()


except NoSuchElementException:
    pass


table = browser.find_element_by_tag_name('tbody')
table_rows = table.find_elements_by_tag_name('tr')

for row in table_rows:
    if 'thesis' in row.text.lower():

        title = row.find_element_by_xpath('./td[1]')
        location = row.find_element_by_xpath('./td[2]')
        date = row.find_element_by_xpath('./td[3]')
        link = title.find_element_by_tag_name('a').get_attribute('href')

        print('Title: {}\nDate: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, date.text, location.text, link))

