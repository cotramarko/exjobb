import browserobject
import re

def crawl():
    browser = browserobject.start_browser("https://boliden.csod.com/ats/careersite/search.aspx?site=5&c=boliden")
    baseurl = "https://boliden.csod.com/ats/careersite/JobDetails.aspx?id="
    COMPANY = 'Boliden'
    #job_list = browser.find_elements_by_tag_name('''li''')
    job_list = browser.find_elements_by_xpath('''//ul/li''')

    list_of_thesis = []

    for l in job_list:
        try:
            title = l.find_element_by_tag_name('a')
            location_data = l.find_element_by_class_name("FieldValue").text
            
        except:
            continue
        department, location = re.findall('\((.*?)\|(.*?)\)', location_data)[0]
        
        link_info = title.get_attribute('href')
        match = re.findall('.*?id=([^"]*)', link_info)
        

        #print('Title: {}\nDepartment: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, department, location, baseurl+match[0]))
        list_of_thesis.append(dict(title= title.text, location = location, link=baseurl+match[0], company = COMPANY))

    if list_of_thesis:
        browser.quit()
        return list_of_thesis
    else:
        return []

if __name__ == '__main__':
    crawl()