
import time


from pynput.keyboard import Key, Controller

from pageObjects.Baseclass import Baseclass
from pageObjects.LoginPage import LoginPage
from pageObjects.PimPage import PimPage
from pageObjects.actionsPerform import actionsPerform

class TestOne(Baseclass):
    def testo2o(self):

        log=self.getLogger()

    #LOGIN PAGE
        log.info("i am in login page")
        loginpage = LoginPage(self.driver)

        loginpage.getUsername().send_keys("Admin")
        loginpage.getPassword().send_keys("admin123")
        #loginpage.getLoginbtn().click()
        pimpageobj = LoginPage.getLoginbtn(self)

    # PIM PAGE
        log.info("i am in PIM page, optimize the page objects")

        pimpageobj.getpimbtn().click()
        pimpageobj.getreports().click()


        #Adding reports
        pimpageobj.getaddreports().click()
        pimpageobj.getreportname().send_keys("abcd")

        pimpageobj.getselectcriteria().click()

        actionsperformobj=actionsPerform(self.driver)
        actionsperformobj.actionshandling()

        log.info("Adding display fields")
        time.sleep(2)
        pimpageobj.getdisplayfieldgroup().click()
        actionsperformobj.actionshandling2()

        pimpageobj.getdisplayfield().click()
        actionsperformobj.actionshandling3()

        pimpageobj.getaddplusfields().click()

        #adding few display fields
        for dsplelem in range(2):
            pimpageobj.getdisplayfield().click()
            time.sleep(2)
            actionsperformobj.actionshandling4()
            self.WaitMethod = pimpageobj.getaddplusfields()
            pimpageobj.getaddplusfields().click()

        time.sleep(2)
        pimpageobj.getincludeHeader().click()
        #save the fields
        pimpageobj.getsavefields().click()
        pimpageobj.getreports().click()

        pimpageobj.getsearchName().send_keys("abc")
        time.sleep(3)
        keyboard=Controller()
        keyboard.press(Key.down)
        keyboard.press(Key.down)
        keyboard.press(Key.enter)

        pimpageobj.getsearchBtn().click()

        self.driver.execute_script("window.scrollTo(600,600);")         #SCROLL
        time.sleep(3)

        #view the name record after search
        pimpageobj.getviewNamerecord().click()
        k=pimpageobj.getverifycustomreport()
        expected_output=["Personal","Employee Id","Employee Last Name","Employee First Name"]

        for element in k:
            txt = element.text
            for exp_str in expected_output:
                try:
                    if exp_str not in txt:                          
                         continue
                except Exception as e:

                    log.error(" Error Occured: records not found", {str(e)})
        else:
            print("Records Found")
            time.sleep(2)
            actionsperformobj.capture_screenshot("img.png")



