import browserobject

def crawl(test = False):
    browser = browserobject.start_browser("http://jobsearch.scania.com/segerjoblist/search.aspx", test)

    COMPANY = "Scania"

    table = browser.find_element_by_id('dgSearchResult')
    table_rows = table.find_elements_by_tag_name('tr')[1:]
    list_of_thesis = []

    for row in table_rows:
        
        if 'examen' in row.text.lower():
            

            title = row.find_element_by_tag_name('a')
            date = row.find_element_by_xpath('./td[1]')
            location = row.find_element_by_xpath('./td[5]')
            app_date = row.find_element_by_xpath('./td[6]')
            link = title.get_attribute('href')


            #print('Title: {}\nDate: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, date.text, location.text, link))
            list_of_thesis.append(dict(title= title.text, location = location.text, link=title.get_attribute('href'), company = COMPANY))

    if list_of_thesis:
        browser.quit()
        return list_of_thesis
    else:
        if not test: browser.quit()
        return []

if __name__ == '__main__':
    crawl()