import browserobject

browser = browserobject.start_browser("http://corporate.vattenfall.se/jobba-hos-oss/jobb/lediga-jobb/?country=Sweden&location=&function=&position=Internship&education=")

COMPANY = "Vattenfall"

table = browser.find_element_by_id('DataTables_Table_0')
table_rows = table.find_elements_by_tag_name('tr')[1:]


for row in table_rows:
    
    
        

    title = row.find_element_by_tag_name('a')
    location = row.find_element_by_xpath('./td[2]')
    date = row.find_element_by_xpath('./td[3]')
    link = title.get_attribute('href')


    print('Title: {}\nDate: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, date.text, location.text, link))
#        list_of_thesis.append(dict(title= title.text, location = location.text, link=title.get_attribute('href')))


