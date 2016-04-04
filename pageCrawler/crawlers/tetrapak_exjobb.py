import browserobject
import time

def crawl():
    browser = browserobject.start_browser("https://tetrapak.taleo.net/careersection/3/jobsearch.ftl?lang=en")

    COMPANY = "Tetra Pak"
    list_of_thesis = []
    #element = browser.find_element_by_xpath("""//*[@id="top"]/div/div[2]/div[5]/div[4]/p[2]/a/strong""")
    #browser.execute_script("return arguments[0].scrollIntoView();", element)

    time.sleep(0.3)
    table = browser.find_element_by_class_name('table')
    table_rows = table.find_elements_by_tag_name('tr')
    #print(table.get_attribute('innerHTML'))

    for row in table_rows:
        
        if 'thesis' in row.text.lower():
            
            title = row.find_element_by_tag_name('a')
            location = row.find_element_by_xpath('./td[2]')
            date = row.find_element_by_xpath('./td[3]')
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
