from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
import json
 

SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

desired_cap = {
    'platformName': os.environ.get('SELENIUM_PLATFORM'),
    'browserName': os.environ.get('SELENIUM_BROWSER'),
    'version': os.environ.get('SELENIUM_VERSION'),
    'deviceName': os.environ.get('SELENIUM_DEVICE'),
    'appiumVersion': "1.5.2"
}

print desired_cap

driver = webdriver.Remote(command_executor = ('http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub'), desired_capabilities = desired_cap)

driver.get('https://www.google.com/')
driver.current_url
driver.page_source
time.sleep(5)
driver.quit()