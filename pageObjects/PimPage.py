from selenium.webdriver.common.by import By


class PimPage:
    def __init__(self,driver):
        self.driver=driver

    pimbtn=(By.XPATH,"//span[text()='PIM']")
    reports=(By.LINK_TEXT,"Reports")
    addreport=(By.XPATH,"//button[text()=' Add ']")
    reportname=(By.CSS_SELECTOR,'input[placeholder="Type here ..."]')
    selectcriteria=(By.XPATH,"(//div[text()='-- Select --'])[1]")
    displayfieldgrp=(By.XPATH,"(//div[contains(@class,'oxd-select-text--after')])[3] ")
    displayfield=(By.XPATH,"(//i[contains(@class,'oxd-select-text--arrow')])[4]")
    addplusfields=(By.XPATH,"(//i[@class='oxd-icon bi-plus'])[2]")
    savefields=(By.XPATH," //button[text()=' Save '] ")
    includeheaderchbx=(By.XPATH,"//span[contains(@class,'oxd-switch-input')]")

    searchName = (By.XPATH,"//input[@placeholder='Type for hints...']")
    searchBtn = (By.XPATH, "//button[@type='submit']")

    viewnamerecord=(By.XPATH,"(//i[@class='oxd-icon bi-file-text-fill']/parent::button)[1]")

    verifycustomreport=(By.CSS_SELECTOR,"div[class='rgHeaderCell']")



    def getpimbtn(self):
        return self.driver.find_element(*PimPage.pimbtn)


    def getreports(self):
        return self.driver.find_element(*PimPage.reports)


    def getaddreports(self):
        return self.driver.find_element(*PimPage.addreport)

    def getreportname(self):
        return self.driver.find_element(*PimPage.reportname)

    def getselectcriteria(self):
        return self.driver.find_element(*PimPage.selectcriteria)
        #actionsperformobj= actionsPerform(self.driver)

    def getdisplayfieldgroup(self):
        return self.driver.find_element(*PimPage.displayfieldgrp)

    def getdisplayfield(self):
        return self.driver.find_element(*PimPage.displayfield)

    def getaddplusfields(self):
        return self.driver.find_element(*PimPage.addplusfields)

    def getincludehearder(self):
        return self.driver.find_element(*PimPage.includeheaderchbx)

    def getincludeHeader(self):
        return self.driver.find_element(*PimPage.includeheaderchbx)

    def getsavefields(self):
        return self.driver.find_element(*PimPage.savefields)

    def getsearchName(self):
        return self.driver.find_element(*PimPage.searchName)

    def getsearchBtn(self):
        return self.driver.find_element(*PimPage.searchBtn)

    def getviewNamerecord(self):
        return self.driver.find_element(*PimPage.viewnamerecord)
    def getverifycustomreport(self):
        return self.driver.find_elements(*PimPage.verifycustomreport)



