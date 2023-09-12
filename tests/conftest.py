import pytest
from selenium import webdriver

#driver=webdriver.Chrome()
#driver.implicitly_wait(5)
@pytest.fixture()
def setup(request):

    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver=driver       #returning the driver obj
    yield
    print("test ended")
    driver.close()
