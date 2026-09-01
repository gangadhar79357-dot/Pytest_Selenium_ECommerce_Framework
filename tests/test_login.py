import pytest
from pages.login_page import LoginPage
from utils.read_config import ReadConfig
from utils.custom_logger import LogGen

@pytest.mark.usefixtures("setup")
class TestLogin:
    baseURL = ReadConfig.get_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_login_valid(self):
        self.logger.info("**** Starting Test_001_Login ****")
        self.driver.get(self.baseURL + "/login")
    
        lp = LoginPage(self.driver)
        lp.login_to_application(self.email, self.password)
    
        actual_title = self.driver.title
        # Changed to partial match for better stability
        if "Automation Exercise" in actual_title:
            self.logger.info("**** Login Test Passed ****")
            assert True
        else:
            self.logger.error(f"**** Login Test Failed: Title Mismatch. Actual: {actual_title} ****")
            self.driver.save_screenshot(".\\reports\\screenshots\\test_login_failed.png")
            assert False