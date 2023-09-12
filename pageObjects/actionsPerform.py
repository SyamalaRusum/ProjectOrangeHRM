from selenium.webdriver import ActionChains, Keys


class actionsPerform:
    def __init__(self,driver):
        self.driver=driver

    def actionshandling(self):
        actions = ActionChains(self.driver)
        actions.send_keys("e")
        actions.send_keys(Keys.ENTER)
        actions.perform()
    def actionshandling2(self):
        actions1 = ActionChains(self.driver)
        actions1.send_keys("p")
        actions1.send_keys(Keys.ENTER)
        actions1.perform()
    def actionshandling3(self):
        actions2 = ActionChains(self.driver)
        actions2.send_keys("e")
        # time.sleep(2)
        actions2.send_keys(Keys.ENTER)
        actions2.perform()

    def actionshandling4(self):
        actions3 = ActionChains(self.driver)
        actions3.send_keys("e")
        actions3.send_keys(Keys.ENTER)
        actions3.perform()

    def capture_screenshot(self,filename):
        self.driver.save_screenshot(filename)