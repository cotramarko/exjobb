import browserobject

def crawl(test = False):
    browser = browserobject.start_browser("http://www.billerudkorsnas.com/sv/Karriar/Lediga-jobb/Exjobb2/", test)
    COMPANY = 'Billerud'

    job_list = browser.find_elements_by_xpath('''//*[@id="primarycontent"]/article/table/tbody/tr''')
    list_of_thesis = []
    for l in job_list:
        
        title = l.find_element_by_class_name('listTitle')
        location = l.find_element_by_xpath('''.//td[2]''')
        link = l.find_element_by_tag_name('a')
        
        #print('Title: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, location.text, link.get_attribute('href')))
        list_of_thesis.append(dict(title= title.text, location = location.text, link=link.get_attribute('href'), company = COMPANY))
    

    if list_of_thesis:
        browser.quit()
        return list_of_thesis
    else:
        if not test: browser.quit()
        return []
    

if __name__ == '__main__':
    crawl()