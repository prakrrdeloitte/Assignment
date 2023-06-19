from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.all_tabs = (By.XPATH, "//div[@id='nav-hamburger-menu']")
        self.mobiles_computers = (By.XPATH, "//div[contains(@aria-label, 'Mobiles, Computers')]")
        self.all_mobile_phones = (By.XPATH, "//div[contains(@aria-label, 'All Mobile Phones')]")

    def click_all_tabs(self):
        self.driver.find_element(*self.all_tabs).click()

    def select_mobiles_computers(self):
        self.driver.find_element(*self.mobiles_computers).click()

    def select_all_mobile_phones(self):
        self.driver.find_element(*self.all_mobile_phones).click()

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.apple_shop_now = (By.XPATH, "//div[@id='appleShopNow']")
        self.iphone_13_pro_max = (By.XPATH, "//div[contains(@aria-label, 'iPhone 13 Pro Max')]")
        self.price = (By.XPATH, "//span[@class='a-price-whole']")
        self.add_to_cart = (By.XPATH, "//input[@id='add-to-cart-button']")
        self.cart_count = (By.ID, "nav-cart-count")

    def select_apple_shop_now(self):
        actions = ActionChains(self.driver)
        apple_shop_now_element = self.driver.find_element(*self.apple_shop_now)
        actions.move_to_element(apple_shop_now_element).perform()
        apple_shop_now_element.click()

    def select_iphone_13_pro_max(self):
        self.driver.find_element(*self.iphone_13_pro_max).click()

    def get_price(self):
        return self.driver.find_element(*self.price).text

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_count).text

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart = (By.ID, "nav-cart")
        self.cart_subtotal = (By.XPATH, "//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap']")

    def click_cart(self):
        self.driver.find_element(*self.cart).click()

    def get_cart_subtotal(self):
        return self.driver.find_element(*self.cart_subtotal).text

# Usage example
driver = webdriver.Chrome()

# Navigate to amazon.in
driver.get("https://www.amazon.in")

home_page = HomePage(driver)

# Click on All tabs on the left side
home_page.click_all_tabs()

# Scroll down and select Mobiles, Computers and then all mobile phones
home_page.select_mobiles_computers()
home_page.select_all_mobile_phones()

product_page = ProductPage(driver)

# Scroll right here and select Apple Shop now option
product_page.select_apple_shop_now()

# Scroll down and click on Buy of iPhone 13 pro max
product_page.select_iphone_13_pro_max()

# Take the price from this page and click on Add to cart
price = product_page.get_price()
product_page.click_add_to_cart()

# Validate "1" is showing on cart option
cart_count = product_page.get_cart_count()
if cart_count == "1":
    print




