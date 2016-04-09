import browserobject
import time

def crawl():
    browser = browserobject.start_browser("http://www.home.sandvik/se/karriar/student/examensarbete/examensarbeten/")

    COMPANY = "Sandvik"
    list_of_thesis = []

    table = browser.find_element_by_tag_name('thead')
    table_rows = table.find_elements_by_tag_name('tr')[1:]

    for row in table_rows:
        title = row.find_element_by_xpath('./th[1]')
        subject = row.find_element_by_xpath('./th[2]')
        location = row.find_element_by_xpath('./th[3]')
        date = row.find_element_by_xpath('./th[4]')
        link = row.find_element_by_tag_name('a')

        list_of_thesis.append(dict(title= subject.text, location = location.text, link=link.get_attribute('href'), company = COMPANY))

    if list_of_thesis:
        browser.quit()
        return list_of_thesis
    else:
        return []

if __name__ == '__main__':
    crawl()