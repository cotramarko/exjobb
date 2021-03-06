import browserobject

def crawl(test = False):
    browser = browserobject.start_browser("https://jobs.ericsson.com/search/?q=&locationsearch=sweden", test)

    COMPANY = "Ericsson"

    if int(browser.find_element_by_xpath("""//*[@id="content"]/div[3]/div/div/span/span[1]/b[2]""").text) > 25:
        second_page = True
    list_of_thesis = []

    table_rows = browser.find_elements_by_css_selector('tr.data-row.clickable')

    for _ in range(2):

        for row in table_rows:

            if 'thesis' in row.text.lower():
                title = row.find_element_by_tag_name('a')
                location = row.find_element_by_xpath('./td[2]')
                date = row.find_element_by_xpath('./td[3]')
                link = title.get_attribute('href')

                #print('Title: {}\nDate: {}\nLocation: {}\nLink: {}\n\n'.format(title.text, date.text, location.text, link))
                list_of_thesis.append(dict(title= title.text, location = location.text, link=link, company = COMPANY))

        if second_page:
            browser.find_element_by_class_name('paginationItemLast').click()
            table_rows = browser.find_elements_by_css_selector('tr.data-row.clickable')
        else:
            break



            

    if list_of_thesis:
        browser.quit()
        return list_of_thesis
    else:
        if not test: browser.quit()
        return []

if __name__ == '__main__':
    crawl()