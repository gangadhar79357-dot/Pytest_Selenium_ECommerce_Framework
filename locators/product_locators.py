from selenium.webdriver.common.by import By

class ProductLocators:
    ALL_PRODUCTS_LINK = (By.XPATH, "//a[@href='/products']")
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCH_RESULT_TITLE = (By.XPATH, "//h2[@class='title text-center']")