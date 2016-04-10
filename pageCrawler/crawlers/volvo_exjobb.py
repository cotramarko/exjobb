import browserobject
import time

def crawl(test = False):
    browser = browserobject.start_browser("https://xjobs.brassring.com/TGWebHost/searchresults.aspx?partnerid=25079&siteid=5171&Codes=Volvo&AgentID=9780452&Function=runquery", test)
    url = 'https://xjobs.brassring.com/TGWebHost/searchresults.aspx?partnerid=25079&siteid=5171&Codes=Volvo&AgentID=9780452&Function=runquery'
    COMPANY = "Volvo Group"
    list_of_thesis = []
    #element = browser.find_element_by_xpath("""//*[@id="top"]/div/div[2]/div[5]/div[4]/p[2]/a/strong""")
    #browser.execute_script("return arguments[0].scrollIntoView();", element)

    time.sleep(0.3)
    table = browser.find_element_by_id('idSearchresults')
    table_rows = table.find_elements_by_tag_name('tr')


    for row in table_rows:
        row.text
        if 'thesis' in row.text.lower():
            
            title = row.find_element_by_tag_name('a')
            location = row.find_element_by_xpath('./td[5]')
            if 'sweden' in location.text.lower():
                continue
            date = row.find_element_by_xpath('./td[3]')
            link = title.get_attribute('href')

            #print('Title: {}\nDate: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, date.text, location.text, url))
            list_of_thesis.append(dict(title= title.text, location = location.text, company = COMPANY, link=url))

    if list_of_thesis:
        browser.quit()
        return list_of_thesis
    else:
        if not test: browser.quit()
        return []


if __name__ == '__main__':
    crawl()