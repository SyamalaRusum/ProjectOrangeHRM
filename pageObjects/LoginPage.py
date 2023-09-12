from selenium.webdriver.common.by import By

from pageObjects.PimPage import PimPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username=(By.NAME,'username')
    password=(By.NAME,'password')
    loginbtn=(By.CSS_SELECTOR,"button[type='submit']")

    def getUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getLoginbtn(self):
       self.driver.find_element(*LoginPage.loginbtn).click()
       pimpageobj = PimPage(self.driver)
       return pimpageobj


