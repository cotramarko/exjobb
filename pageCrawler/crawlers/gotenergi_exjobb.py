import browserobject
import time

def crawl(test = False):
    browser = browserobject.start_browser("http://www.goteborgenergi.se/Om_oss/Karriar/Student/Examensarbete", test)

    COMPANY = "Göteborgs Energi"
    time.sleep(0.3)
    table = browser.find_element_by_class_name('Dx-Content-Table')
    table_rows = table.find_elements_by_tag_name('tr')[1:]

    list_of_thesis = []

    for row in table_rows:
        
        title = row.find_element_by_tag_name('a')
        location = 'Gothenburg'
        link = title.get_attribute('href')

        #print('Title: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, location, link))
        list_of_thesis.append(dict(title= title.text, location = location, link=title.get_attribute('href'), company = COMPANY))

    if list_of_thesis:
        browser.quit()
        return list_of_thesis
    else:
        if not test: browser.quit()
        return []


if __name__ == '__main__':
    crawl()