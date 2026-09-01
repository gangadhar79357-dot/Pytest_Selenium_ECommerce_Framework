from pages.base_page import BasePage
from locators.checkout_locators import CheckoutLocators

class CheckoutPage(BasePage):
    
    def add_first_product_to_cart(self):
        # JS Click avoids the Ad Interception error we saw earlier
        self.click_element_js(CheckoutLocators.FIRST_PRODUCT_ADD_CART)
        # We don't need to click 'Continue Shopping' if we navigate via the header Cart link

    def navigate_to_cart(self):
        # Clicking Cart in the header is the most reliable way to reach the cart
        self.click_element_js(CheckoutLocators.HEADER_CART_LINK)

    def proceed_to_checkout(self):
        self.click_element_js(CheckoutLocators.PROCEED_CHECKOUT_BTN)

    def place_order(self, message):
        self.type_text(CheckoutLocators.MESSAGE_TEXTAREA, message)
        self.click_element_js(CheckoutLocators.PLACE_ORDER_BTN)