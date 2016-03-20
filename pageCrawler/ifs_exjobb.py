import browserobject

browser = browserobject.start_browser("http://www.ifsworld.com/se/verksamheten/arbeta-hos-oss/lediga-jobb/apply-for-a-job/")

COMPANY = "IFS"

browser.switch_to_frame("riframe") 
table = browser.find_element_by_id('jobsTable')
#print(table.get_attribute('innerHTML'))
table_rows = table.find_elements_by_tag_name('tr')[1:]


for row in table_rows:
    if 'thesis' in row.text.lower():

        title = row.find_element_by_tag_name('a')
        location = row.find_element_by_xpath('./td[3]')
        date = row.find_element_by_xpath('./td[2]')
        link = title.get_attribute('href')

        print('Title: {}\nDate: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, date.text, location.text, link))
#        list_of_thesis.append(dict(title= title.text, location = location.text, link=title.get_attribute('href')))


