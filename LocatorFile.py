from selenium.webdriver.common.by import By

#Main Page


mainPageEmailFieldLocator = (By.ID, "ap_email")
mainPageContinueButtonLocator = (By.ID, "continue")
mainPagePasswordFieldLocator = (By.ID, "ap_password")
mainPageSigninButtonLocator = (By.ID, "signInSubmit")



#Main page

MainPageCartSectionButtonLocator = (By.ID, "nav-cart-count")


#Card Section

CartSectionDeleteButtonLocator = (By.XPATH, "(//input[@value ='Delete'])[1]")
CartSectionDeleteButtonLocatorAll = (By.XPATH, "//input[@value='Delete']")