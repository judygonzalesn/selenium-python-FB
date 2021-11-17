from selenium import webdriver
from page import send_Goodnight
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import unittest


# driver = webdriver.Chrome(ChromeDriverManager().install())

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:0914")
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(executable_path="C:\\Python\\Selenium\\chromedriver.exe", options=self.chrome_options)
        self.driver.get("https://www.facebook.com/messages/t/[senderFBUsername]")
        # self.driver.get("https://www.facebook.com/messages/t/[recieverFBUsername]")
        self.driver.implicitly_wait(10)

    def test_search_in_python_org(self):
        driver = self.driver
        search = send_Goodnight(driver)
        search.send_goodnightFunction()

        if __name__ == "__main__":
            unittest.main()
