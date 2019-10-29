from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time
browser = webdriver.Firefox()
print "WebDriver Object", browser

browser.maximize_window()
browser.get('https://facebook.com')