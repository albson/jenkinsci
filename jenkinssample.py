from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
import json
 

SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

test_name = "TesterReporter"

desired_cap = {
    'platform': os.environ.get('SELENIUM_PLATFORM'),
    'browserName': os.environ.get('SELENIUM_BROWSER'),
    'version': os.environ.get('SELENIUM_VERSION'),
    'name': test_name,
    'build': "testbuilder01"
#     'build': os.environ.get('JENKINS_BUILD_NUMBER')
#     'name': "Jenkins Sample Test",
#     'tunnelIdentifier': os.environ.get('TUNNEL_IDENTIFIER')
#     'tunnelIdentifier': 'tunnel1'
}

print desired_cap

driver = webdriver.Remote(command_executor = ('http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub'), desired_capabilities = desired_cap)

driver.get('http://example.com/')
driver.current_url
driver.page_source
session = driver.session_id
print "SauceOnDemandSessionID=" + session + " job-name=" + test_name
time.sleep(3)
driver.quit()
