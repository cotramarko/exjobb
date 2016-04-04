import browserobject


def crawl():
    browser = browserobject.start_browser("")

    COMPANY = "Sandvik"

    table = browser.find_element_by_tag_name('tbody')
    table_rows = table.find_element_by_tag_name('tr')

    for row in table_rows:
        title = row.find_element_by_xpath('./td[1]')
        subject = row.find_element_by_xpath('./td[2]')
        location = row.find_element_by_xpath('./td[3]')
        date = row.find_element_by_xpath('./td[4]')
        link = 'how to fetch link'

if __name__ == '__main__':
    crawl()