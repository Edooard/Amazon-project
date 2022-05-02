from selenium.webdriver.common.by import By
from Locators.LocatorFile import *

class MainPageClass():
    def __init__(self, driver):
        self.driver = driver

    def fill_email_field(self, text):
        emailField = self.driver.find_element(*mainPageEmailFieldLocator)
        emailField.clear()
        emailField.send_keys(text)

    def press_continue_button(self):
        continueButton = self.driver.find_element(*mainPageContinueButtonLocator)
        continueButton.click()

    def input_password_field(self, text):
        passwordField = self.driver.find_element(*mainPagePasswordFieldLocator)
        passwordField.send_keys(text)

    def press_sign_in_button(self):
        signinButton = self.driver.find_element(*mainPageSigninButtonLocator)
        signinButton.click()


