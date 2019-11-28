from selenium import webdriver
from applitools.selenium import Eyes, Target
from applitools.common.config import BatchInfo
import os

class ChromeSetupAI(object):
    """
    run the tests in UserStoryTests in Chrome
    """
    eyes = Eyes()
    os.environ['APPLITOOLS_API_KEY'] = '9HUjLRImIJJ108H0eSoRYU5lYUxa7UoKjWqmdx9k89jpk110'
    eyes.api_key = os.environ['APPLITOOLS_API_KEY']

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./TraditionalTestFramework/Drivers/chromedriver')
        self.driver.get(self.url)
        self.driver.set_window_size(1680, 800)
        self.driver.set_script_timeout(1)

    def setBatching(self, value):
        b = BatchInfo(value)
        b.id_ = value
        self.eyes.batch = b
        self.eyes.open(self.driver, "Test app", value, {'width': 1680, 'height': 800}) 
        self.eyes.force_full_page_screenshot = True
        self.eyes.use_css_transition = True

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        self.eyes.close()

class ChromeSetupDefault(object):
    """
    run the tests in UserStoryTests in Chrome
    """
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./TraditionalTestFramework/Drivers/chromedriver')
        self.driver.get(self.url)
        self.driver.set_script_timeout(1)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        