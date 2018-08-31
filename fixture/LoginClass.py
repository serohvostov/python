class LoginClass:
    def __init__(self, app):
        self.app = app

    def login(self, SiteClass):
        wd = self.app.wd
        wd.find_element_by_css_selector("h1.title").click()
        wd.find_element_by_css_selector("a.dropdown-toggle").click()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(SiteClass.username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("demo-admin")
        wd.find_element_by_css_selector("body").click()
        wd.find_element_by_css_selector("a.dropdown-toggle").click()
        wd.find_element_by_name("login").click()

    def link(self, SiteClass):
        wd = self.app.wd
        wd.find_element_by_name("link-url").click()
        wd.find_element_by_name("link-url").clear()
        wd.find_element_by_name("link-url").send_keys(SiteClass.sitename)
        wd.find_element_by_id("shorten").click()