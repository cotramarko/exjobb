import browserobject

browser = browserobject.start_browser("http://saabgroup.com/sv/career/job-opportunities/?&c=Sweden")

COMPANY = "SAAB"
#element = browser.find_element_by_xpath("""//*[@id="top"]/div/div[2]/div[5]/div[4]/p[2]/a/strong""")
#browser.execute_script("return arguments[0].scrollIntoView();", element)


table = browser.find_element_by_class_name('vacancies')
table_rows = table.find_elements_by_tag_name('li')

for row in table_rows:
    if 'examen' in row.text.lower():
        print(row.text)
        title = find_element_by_class_name('title')
        location = find_elements_by_tag_name('location')
        date = find_element_by_class_name('date')
        link = title.get_attribute('href')


#        list_of_thesis.append(dict(title= title.text, location = location.text, link=title.get_attribute('href')))


