import browserobject
import time

def crawl():
    browser = browserobject.start_browser("http://www.afconsult.com/sv/jobba-hos-oss/lediga-jobb/")
    COMPANY = 'ÅF'
    time.sleep(1)    #might need to explicitly wait for website to load

    find_button = browser.find_element_by_id("""dk1-combobox""").click() #category
    option = browser.find_element_by_id("dk1--2024534255__jobFilters").click() #

    time.sleep(1)
    content = browser.find_element_by_id("contentItemListing_6373")
    job_list = content.find_elements_by_css_selector('.block.col.regular-12')
    list_of_thesis = []

    for l in job_list:
        title = l.find_element_by_css_selector(".col.regular-6")
        if "exjobb" in title.text.lower():
            #print(title.text)
            link = l.find_element_by_tag_name("a")
            location, app_date = l.find_elements_by_css_selector(".col.regular-3")

            #print('Title: {}\nLocation: {}\nApplication Date: {}\n\n'.format(title.text, location.text, app_date.text, link.get_attribute('href')))

            list_of_thesis.append(dict(title= title.text, location = location.text, link=link.get_attribute('href'), company = COMPANY))

    if list_of_thesis:
        return list_of_thesis
    else:
        return []

    browser.quit()

if __name__ == '__main__':
    crawl()