from selenium import webdriver
import unittest
import time
from Pages.MainPage import MainPageClass
from Pages.HomePage import HomePageClass
from Pages.CartPage import CartPageClass

class myGoogleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.mainPage = MainPageClass(self.driver)
        self.homePage = HomePageClass(self.driver)
        self.cartPage = CartPageClass(self.driver)

    def test_myTest(self):
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

        self.mainPage.fill_email_field("eduard.iskandarian@gmail.com")
        time.sleep(1)
        self.mainPage.press_continue_button()
        time.sleep(1)
        self.mainPage.input_password_field("091313059")
        time.sleep(1)
        self.mainPage.press_sign_in_button()
        time.sleep(1)
        self.homePage.press_cart_button()
        time.sleep(1)
        self.cartPage.press_delete_button()



    def tearDown(self):
        time.sleep(4)
        self.driver.close()