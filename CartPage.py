from selenium.webdriver.common.by import By
from Locators.LocatorFile import *
from Common.CustomFind.FindElement import FindElement
import time

class CartPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.FindElement = FindElement(self.driver)

    def delete_all_items_from_cart(self):
        cartItemsCount = self.FindElement.find(*MainPageCartSectionButtonLocator)
        numberCartItemsCount = int(cartItemsCount.text)
        try:
            while numberCartItemsCount > 0:
                deleteItemsButton = self.driver.find_element(*CartSectionDeleteButtonLocatorAll)
                deleteItemsButton.click()
                numberCartItemsCount -= 1
                time.sleep(2)
        except:
            pass

