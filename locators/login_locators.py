from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGOUT_LINK = (By.XPATH, "//a[contains(text(),'Logout')]")