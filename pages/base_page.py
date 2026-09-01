from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_element(self, locator):
        """Wait for element to be present and return it"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """Wait for element to be clickable and click it"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_element_js(self, locator):
        """Clicks an element using JavaScript - bypasses Ad overlays"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        """Find element and type text"""
        self.find_element(locator).send_keys(text)

    def upload_file(self, locator, file_path):
        """Handles file uploads by sending the file path to the input element"""
        self.find_element(locator).send_keys(file_path)

    def handle_alert(self):
        """Waits for browser alert to appear and accepts it"""
        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def get_title(self):
        """Returns the current page title"""
        return self.driver.title

    def get_text(self, locator):
        """Returns the inner text of a specific element"""
        return self.find_element(locator).text