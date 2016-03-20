import browserobject

browser = browserobject.start_browser("http://new.abb.com/se/jobba-hos-oss/lediga-tjanster")

#element has to be in view to click -> scroll to element
find_button = browser.find_element_by_class_name("""findButton""")
filter_selection = browser.find_element_by_xpath("""//*[@id="Content_C001_Col00"]/div/div[2]/div[3]/span[4]/div/a/span""")
browser.execute_script("return arguments[0].scrollIntoView();", find_button)
filter_selection.click()
browser.find_element_by_xpath("""//*[@data-option-array-index='4']""").click()
time.sleep(0.5) #time for content to load
job_list = browser.find_elements_by_xpath("""//*[@id="jobOffers"]/tbody/tr""")

list_of_thesis = []

for l in job_list:
    #print (l.text)
    title = l.find_element_by_tag_name('a')
    _, location, department, job_type, _  = l.find_elements_by_tag_name('td')
    print('Title: {}\nLocation: {}\nDepartment: {}\nLink: {}\n\n'.format(title.text, location.text, department.text, title.get_attribute('href')))

    list_of_thesis.append(dict(title= title.text, location = location.text, link=title.get_attribute('href')))

if list_of_thesis:
    #json_append.update_json(list_of_thesis)
    pass