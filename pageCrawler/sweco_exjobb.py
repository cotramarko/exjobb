import browserobject

def crawl():
    browser = browserobject.start_browser("http://www.sweco.se/sv/Sweden/Karriar/Lediga-jobb1/")

    COMPANY = "Sweco"
    list_of_thesis = []

    browser.switch_to_frame("riframe") 
    table = browser.find_element_by_id('jobsTable')
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
