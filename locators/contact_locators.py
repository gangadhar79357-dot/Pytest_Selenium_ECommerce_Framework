from selenium.webdriver.common.by import By

class ContactLocators:
    CONTACT_US_LINK = (By.XPATH, "//a[contains(text(),'Contact us')]")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    SUBJECT_INPUT = (By.NAME, "subject")
    MESSAGE_INPUT = (By.ID, "message")
    UPLOAD_FILE = (By.NAME, "upload_file")
    SUBMIT_BTN = (By.NAME, "submit")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".contact-form .alert-success")