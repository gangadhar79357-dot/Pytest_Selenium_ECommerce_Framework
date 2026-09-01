import pytest
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from utils.read_config import ReadConfig
from utils.custom_logger import LogGen

@pytest.mark.usefixtures("setup")
class TestCheckout:
    baseURL = ReadConfig.get_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_end_to_end_checkout(self):
        self.logger.info("**** Starting Test_002_E2E_Checkout ****")
        
        # 1. Login
        self.driver.get(self.baseURL + "/login")
        lp = LoginPage(self.driver)
        lp.login_to_application(self.email, self.password)
        self.logger.info("Logged in successfully")

        # 2. Add Product
        cp = CheckoutPage(self.driver)
        cp.add_first_product_to_cart()
        self.logger.info("Product added to cart")

        # 3. Navigate to Cart
        cp.navigate_to_cart()
        self.logger.info("Navigated to Cart")

        # 4. Proceed and Place Order
        cp.proceed_to_checkout()
        cp.place_order("Professional E2E Test Order.")
        self.logger.info("Order placed")
        
        # 5. Verify Result
        current_url = self.driver.current_url
        if "payment" in current_url.lower():
            self.logger.info("**** E2E Checkout Test Passed ****")
            assert True
        else:
            # This is the line that was broken - now fixed:
            self.logger.error(f"Failed to reach payment page. URL: {current_url}")
            self.driver.save_screenshot(".\\reports\\screenshots\\checkout_failed.png")
            assert False