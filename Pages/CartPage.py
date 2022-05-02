from selenium.webdriver.common.by import By
from Locators.LocatorFile import *
import time

class CartPageClass():
    def __init__(self, driver):
        self.driver = driver

    def delete_all_items_from_cart(self):
        cartItemsCount = self.driver.find_element(*MainPageCartSectionButtonLocator)
        numberCartItemsCount = int(cartItemsCount.text)
        try:
            while numberCartItemsCount > 0:
                deleteItemsButton = self.driver.find_element(*CartSectionDeleteButtonLocatorAll)
                deleteItemsButton.click()
                numberCartItemsCount -= 1
                time.sleep(2)
        except:
            pass

