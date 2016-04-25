#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""This test assumes SAUCE_USERNAME and SAUCE_ACCESS_KEY are environment variables
set to your Sauce Labs username and access key."""

#importing the unittest python module that provides classes for test automation.
import unittest
#importing the time python module that supports time related functions.
import time
#importing the os module which provides a portable way of using operating system dependent functionality.
import os
#importing the sys module which provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import sys
#importing the Selenium Python bindings for Selenium Webdriver from the python Selenium module.
from selenium import webdriver
#importing  the sauceclient which is a Python client library, used for accessing the Sauce Labs REST API to retrieve and update information about resources.
import sauceclient
import json
import new

#Retreiving enviroment variables
SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

print (SAUCE_USERNAME, SAUCE_ACCESS_KEY)

#Credentials for SauceClient
test_result = sauceclient.SauceClient(SAUCE_USERNAME, SAUCE_ACCESS_KEY)

#Retreiving enviroment variables from Jenkins Plugin
host = os.environ.get('SELENIUM_HOST')
port = os.environ.get('SELENIUM_PORT')
platform = os.environ.get('SELENIUM_PLATFORM')
version = os.environ.get('SELENIUM_VERSION')
browser = os.environ.get('SELENIUM_BROWSER')
device = os.environ.get('SELENIUM_DEVICE')
deviceType = os.environ.get('SELENIUM_DEVICE_TYPE')
driver = os.environ.get('SELENIUM_DRIVER')
onDemandBrowsers = os.environ.get('SAUCE_ONDEMAND_BROWSERS')
url = os.environ.get('SELENIUM_URL')
userName = os.environ.get('SAUCE_USER_NAME')
apiKey = os.environ.get('SAUCE_API_KEY')
startingUrl = os.environ.get('SELENIUM_STARTING_URL')

print (host,port,platform,version,browser,device,deviceType,driver,onDemandBrowsers,url,userName,apiKey,startingUrl)

class DesktopTest(unittest.TestCase):
    def setUp(self):

        self.desired_capabilities = {}
        self.desired_capabilities['browserName'] = os.environ.get('SELENIUM_BROWSER')
        self.desired_capabilities['platform'] = os.environ.get('SELENIUM_PLATFORM')
        self.desired_capabilities['version'] = os.environ.get('SELENIUM_VERSION')
        self.desired_capabilities['name'] = 'Example from Jenkins with Sauce OnDemand Plugin'

        self.driver = webdriver.Remote(command_executor = ('http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub'), desired_capabilities = self.desired_capabilities)
        self.driver.implicitly_wait(30)

    def test_https(self):
        self.driver.get('https://www.saucelabs.com')
        title = self.driver.title
        self.assertEquals("Sauce Labs: Selenium Testing, Mobile Testing, JS Unit Testing and More", title)
        time.sleep(10)
        self.driver.get('http://www.theuselessweb.com/')
        title2 = self.driver.title
        self.assertEquals("The Useless Web", title2)
        time.sleep(10)

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        #using the sauce client to set the pass or fail flags for this test according to the assertions results.
        try:
            if sys.exc_info() == (None, None, None):
                test_result.jobs.update_job(self.driver.session_id, passed=True)
            else:
                test_result.jobs.update_job(self.driver.session_id, passed=False)
        finally:
            self.driver.quit()

if __name__ == '__main__':
        unittest.main()
