from selenium import webdriver

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
import os


def start_browser(url, test):
    PATH = os.environ["PATH"].split(':',1)[0]
    PATH = '/usr/local/bin' if PATH == '/usr/bin' else PATH

    if test:
        chromedriver = PATH + "/chromedriver" #change to local chromedriver location
        os.environ["webdriver.chrome.driver"] = chromedriver
        browser = webdriver.Chrome(chromedriver)
    else:
        phantomjs = PATH + "/phantomjs"
        browser = webdriver.PhantomJS(phantomjs)
    browser.maximize_window()
    browser.get(url)
    return browser



#now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#browser.get_screenshot_as_file('screenshot-%s.png' % now)