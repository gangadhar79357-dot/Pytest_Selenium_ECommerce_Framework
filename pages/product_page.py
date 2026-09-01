from pages.base_page import BasePage
from locators.product_locators import ProductLocators

class ProductPage(BasePage):
    def search_for_product(self, product_name):
        self.click_element(ProductLocators.ALL_PRODUCTS_LINK)
        self.type_text(ProductLocators.SEARCH_INPUT, product_name)
        self.click_element(ProductLocators.SEARCH_BUTTON)

    def get_search_title(self):
        return self.find_element(ProductLocators.SEARCH_RESULT_TITLE).text