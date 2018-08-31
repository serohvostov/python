from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.LoginClass import LoginClass

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.loginn = LoginClass(self)

    def open_browser(self):
        wd = self.wd
        wd.get("http://demo.polr.me/")

    def tearDown(self):
        self.wd.quit()