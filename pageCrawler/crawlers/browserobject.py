from selenium import webdriver

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
import os


def start_browser(url):
    PATH = os.environ["PATH"].split(':',1)[0]
    PATH = '/usr/local/bin' if PATH == '/usr/bin' else PATH

    chromedriver = PATH + "/chromedriver" #change to local chromedriver location
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome(chromedriver)

    browser.get(url)

    return browser

