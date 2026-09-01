from selenium.webdriver.common.by import By

class CheckoutLocators:
    # Adding to cart
    FIRST_PRODUCT_ADD_CART = (By.XPATH, "(//div[@class='productinfo text-center']//a[contains(text(),'Add to cart')])[1]")
    
    # Navigation to Cart (Header link is the most stable)
    HEADER_CART_LINK = (By.XPATH, "//a[contains(text(),'Cart')]")
    
    # Checkout Process
    PROCEED_CHECKOUT_BTN = (By.CSS_SELECTOR, ".check_out")
    MESSAGE_TEXTAREA = (By.NAME, "message")
    PLACE_ORDER_BTN = (By.XPATH, "//a[contains(text(),'Place Order')]")