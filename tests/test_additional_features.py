import pytest
import os
from pages.product_page import ProductPage
from pages.contact_page import ContactPage
from utils.read_config import ReadConfig
from utils.custom_logger import LogGen

@pytest.mark.usefixtures("setup")
class TestAdditionalFeatures:
    baseURL = ReadConfig.get_url()
    logger = LogGen.loggen()

    def test_search_product(self):
        self.logger.info("**** Starting Search Product Test ****")
        self.driver.get(self.baseURL)
        pp = ProductPage(self.driver)
        pp.search_for_product("T-Shirt")
        assert "SEARCHED PRODUCTS" in pp.get_search_title()
        self.logger.info("Search test passed")

    def test_contact_us_form(self):
        self.logger.info("**** Starting Contact Us Test ****")
        self.driver.get(self.baseURL)
        cp = ContactPage(self.driver)
        cp.navigate_to_contact_us()
        
        # Create a real temporary file to upload
        file_path = os.path.abspath("upwork_sample.txt")
        with open(file_path, "w") as f:
            f.write("This is a sample file for automation upload test.")

        cp.fill_contact_form(
            "Ganga Tester", 
            "test@example.com", 
            "Portfolio Project", 
            "Testing file upload and alert handling.", 
            file_path
        )
        
        success_msg = cp.get_success_message()
        if "Success!" in success_msg:
            self.logger.info("Contact Us form test PASSED")
            assert True
        else:
            self.logger.error("Contact Us form test FAILED")
            assert False
            
        # Clean up: delete the file after test
        os.remove(file_path)