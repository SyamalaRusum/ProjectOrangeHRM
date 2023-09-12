import logging

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class Baseclass:
    def WaitMethod(self):
        waitobj=WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable())


    def getLogger(self):
        logger=logging.getLogger(__name__)
        filehandler=logging.FileHandler('logfile.log')
        formatter=logging.Formatter("%(asctime)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger