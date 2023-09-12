from selenium import webdriver
class example:
    def meth(self):
        driver=webdriver.Chrome()
        driver.get("https://www.google.com")
        print(driver.title)
obj=example()
obj.meth()