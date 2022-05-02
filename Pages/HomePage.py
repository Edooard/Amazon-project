from Locators.LocatorFile import *
class HomePageClass():
    def __init__(self, driver):
        self.driver = driver
        
    def  press_cart_button (self):
           cartButton = self.driver.find_element (*MainPageCartSectionButtonLocator)
           cartButton.click()