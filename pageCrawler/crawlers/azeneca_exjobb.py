import browserobject
browser = browserobject.start_browser("http://jobs.astrazeneca.com")


#element = browser.find_element_by_xpath("""//*[@id="top"]/div/div[2]/div[5]/div[4]/p[2]/a/strong""")
#browser.execute_script("return arguments[0].scrollIntoView();", element)


browser.find_element_by_id("316").click() #sweden
time.sleep(1)
browser.find_element_by_id("1257").click() #student opportunities
time.sleep(1)
browser.find_element_by_class_name('submit').click()

job_list = browser.find_elements_by_class_name('job-res-description')
list_of_thesis = []

for l in job_list:
    
    title = l.find_element_by_class_name('job-title')
    if 'diploma' in title.text.lower():
        location = l.find_element_by_class_name('locations')
        print('Title: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, location.text, title.get_attribute('href')))

        list_of_thesis.append(dict(title= title.text, location = location.text, link=title.get_attribute('href')))


if list_of_thesis:
    pass