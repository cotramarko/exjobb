import browserobject

browser = browserobject.start_browser("http://saabgroup.com/sv/career/job-opportunities/?&c=Sweden")

COMPANY = "Sandvik"

table = browser.find_element_by_tag_name('tbody')
table_rows = table.find_element_by_tag_name('tr')

for row in table_rows:
    title = row.find_element_by_xpath('./td[1]')
    subject = row.find_element_by_xpath('./td[2]')
    location = row.find_element_by_xpath('./td[3]')
    date = row.find_element_by_xpath('./td[4]')
    link = 'how to fetch link'