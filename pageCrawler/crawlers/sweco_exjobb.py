import browserobject
from selenium.common.exceptions import WebDriverException
import time

def crawl():
    browser = browserobject.start_browser("http://www.sweco.se/karriar/lediga-jobb/")

    COMPANY = "Sweco"
    list_of_thesis = []

    
    #show all jobs
    more_jobs_button = browser.find_element_by_class_name('jobsearchresult__link')
    try:
        while True:
            more_jobs_button.click()
            time.sleep(0.2) #delay to wait for content to load
    except WebDriverException:
        print('all jobs naow')

    
    table = browser.find_element_by_class_name('jobsearchresult__table')
    table_rows = table.find_elements_by_tag_name('tr')[1:]

    for row in table_rows:
        
        if any(word in row.text.lower() for word in ['examen','exjobb']):
        
            

            title = row.find_element_by_tag_name('a')
            date = row.find_element_by_xpath('./td[2]')
            location = row.find_element_by_xpath('./td[3]')
            link = title.get_attribute('href')


            #print('Title: {}\nDate: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, date.text, location.text, link))
            list_of_thesis.append(dict(title= title.text, location = location.text, link=title.get_attribute('href'), company = COMPANY))


    if list_of_thesis:
        browser.quit()
        return list_of_thesis
    else:
        return []


if __name__ == '__main__':
    crawl()
