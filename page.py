class send_Goodnight():

    def __init__(self, driver):
        self.driver = driver

        self.TYPE_MESSAGE = '[aria-label="Type a message..."]'
        self.SEND = '[aria-label="Send"]'
        self.HEART_BUTTON = '[title="Send a Like"]'

    def send_goodnightFunction(self):
        self.driver.find_element_by_css_selector(self.TYPE_MESSAGE).send_keys("Goodnight")
        self.driver.find_element_by_css_selector(self.SEND).click()
        self.driver.find_element_by_css_selector(self.TYPE_MESSAGE).send_keys("Sweetdreams")
        self.driver.find_element_by_css_selector(self.SEND).click()
        self.driver.find_element_by_css_selector(self.TYPE_MESSAGE).send_keys("iloveyousomuch")
        self.driver.find_element_by_css_selector(self.SEND).click()
        self.driver.find_element_by_css_selector(self.HEART_BUTTON).click()
