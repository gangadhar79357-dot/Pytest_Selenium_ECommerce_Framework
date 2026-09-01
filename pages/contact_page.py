from pages.base_page import BasePage
from locators.contact_locators import ContactLocators

class ContactPage(BasePage):
    
    def navigate_to_contact_us(self):
        self.click_element(ContactLocators.CONTACT_US_LINK)

    def fill_contact_form(self, name, email, subject, message, file_path):
        self.type_text(ContactLocators.NAME_INPUT, name)
        self.type_text(ContactLocators.EMAIL_INPUT, email)
        self.type_text(ContactLocators.SUBJECT_INPUT, subject)
        self.type_text(ContactLocators.MESSAGE_INPUT, message)
        
        # Using the new upload method from BasePage
        self.upload_file(ContactLocators.UPLOAD_FILE, file_path)
        
        # Submit the form
        self.click_element(ContactLocators.SUBMIT_BTN)
        
        # Using the new alert handler from BasePage
        self.handle_alert()

    def get_success_message(self):
        return self.get_text(ContactLocators.SUCCESS_MSG)