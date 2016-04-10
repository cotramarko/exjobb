import browserobject

def crawl(test = False):
    browser = browserobject.start_browser("http://jobs.gecareers.com/search?q=thesis", test)

    COMPANY = "General Electric"
    list_of_thesis = []
    table = browser.find_element_by_id('searchresults')
    table_rows = table.find_elements_by_tag_name('tr')[2:]


    for row in table_rows:
        
        if 'thesis' in row.text.lower() and 'sweden' in row.text.lower():

            title = row.find_element_by_tag_name('a')
            location = row.find_element_by_xpath('./td[2]')
            date = row.find_element_by_xpath('./td[3]')
            link = title.get_attribute('href')

            #print('Title: {}\nDate: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, date.text, location.text, link))
            list_of_thesis.append(dict(title= title.text, location = location.text, link=link, company = COMPANY))

    if list_of_thesis:
        browser.quit()
        return list_of_thesis
    else:
        if not test: browser.quit()
        return []


if __name__ == '__main__':
    crawl()