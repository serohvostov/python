# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test(self):
        success = True
        wd = self.wd
        wd.get("http://demo.polr.me/")
        wd.find_element_by_css_selector("h1.title").click()
        wd.find_element_by_css_selector("a.dropdown-toggle").click()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("demo-admin")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("demo-admin")
        wd.find_element_by_css_selector("body").click()
        wd.find_element_by_css_selector("a.dropdown-toggle").click()
        wd.find_element_by_name("login").click()
        wd.find_element_by_name("link-url").click()
        wd.find_element_by_name("link-url").clear()
        wd.find_element_by_name("link-url").send_keys("https://confluence.speechpro.com/pages/viewpage.action?pageId=70233033")
        wd.find_element_by_id("shorten").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
