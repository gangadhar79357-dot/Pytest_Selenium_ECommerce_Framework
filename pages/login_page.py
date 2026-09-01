from pages.base_page import BasePage
from locators.login_locators import LoginLocators # Import the locators

class LoginPage(BasePage):
    
    # We no longer define locators here. We use LoginLocators class.

    def login_to_application(self, email, password):
        self.type_text(LoginLocators.EMAIL_INPUT, email)
        self.type_text(LoginLocators.PASSWORD_INPUT, password)
        self.click_element(LoginLocators.LOGIN_BUTTON)

    def is_logout_visible(self):
        return self.find_element(LoginLocators.LOGOUT_LINK).is_displayed()