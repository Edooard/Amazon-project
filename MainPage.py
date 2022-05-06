from selenium.webdriver.common.by import By
from Locators.LocatorFile import *
from Common.CustomFind.FindElement import FindElement

class MainPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.FindElement = FindElement(self.driver)

    def fill_email_field(self, text):
        emailField = self.FindElement.find(*mainPageEmailFieldLocator)
        emailField.clear()
        emailField.send_keys(text)

    def press_continue_button(self):
        #continueButton = self.driver.find_element(*mainPageContinueButtonLocator)
        continueButton = self.FindElement.find(*mainPageContinueButtonLocator)
        continueButton.click()

    def input_password_field(self, text):
        passwordField = self.FindElement.find(*mainPagePasswordFieldLocator)
        passwordField.send_keys(text)

    def press_sign_in_button(self):
        signinButton = self.FindElement.find(*mainPageSigninButtonLocator)
        signinButton.click()


