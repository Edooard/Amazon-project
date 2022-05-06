from Locators.LocatorFile import *
from Common.CustomFind.FindElement import FindElement

class HomePageClass():
    def __init__(self, driver):
        self.driver = driver
        self.FindElement = FindElement(self.driver)
        
    def  press_cart_button (self):
           cartButton = self.FindElement.find(*MainPageCartSectionButtonLocator)
           cartButton.click()