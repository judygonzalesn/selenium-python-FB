from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""


class MessengerPageLocators(object):
    TYPE_MESSAGE = (By.CSS_SELECTOR, '[aria-label="Type a message..."]')
    SEND = (By.CSS_SELECTOR, '[aria-label="Send"]')
    HEART_BUTTON = (By.CSS_SELECTOR, '[title="Send a Like"]')
