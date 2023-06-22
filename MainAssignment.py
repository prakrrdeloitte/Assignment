import logging
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Configure logger
from Makemytrip import driver

logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Configure HTML TestRunner for generating test reports
# Replace 'path_to_report_directory' with the actual path where you want to save the report
import HTMLTestRunner

report_file = open('test_report.html', 'w')
test_runner = HTMLTestRunner.HTMLTestRunner(stream=report_file, verbosity=2,
                                            title='Test Report', description='Test Results')

# Define a base test case class with screenshot capture functionality
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        if self._outcome.errors:
            # Capture screenshot if test case failed
            self._capture_screenshot()
        self.driver.quit()

    def _capture_screenshot(self):
        # Get the test case name
        test_name = self._testMethodName

        # Generate a unique filename for the screenshot
        timestamp = time.strftime('%Y%m%d_%H%M%S', time.localtime())
        screenshot_file = f'{test_name}_{timestamp}.png'

        # Save the screenshot
        self.driver.save_screenshot(screenshot_file)
        logging.error(f'Screenshot saved: {screenshot_file}')

# Define test cases
class FlipkartTest(BaseTestCase):
    def test_add_items_to_cart(self):
        driver = self.driver
        driver.get('https://www.flipkart.com')

        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()
    def test_compare_macbooks(self):
        driver = self.driver
        driver.get('https://www.flipkart.com')



    def test_search_flights(self):
        driver = self.driver
        driver.get('https://www.flipkart.com')

    wait = WebDriverWait(self.driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='fromCity']")))

    # Select round trip
    round_trip_radio = driver.find_element(By.XPATH, "//li[@data-cy='roundTrip']")
    round_trip_radio.click()

    # From- Bengaluru
    from_city_input = driver.find_element(By.XPATH, "//input[@id='fromCity']")
    from_city_input.clear()
    from_city_input.send_keys("Bengaluru")

    # To- Pune
    to_city_input = driver.find_element(By.XPATH, "//input[@id='toCity']")
    to_city_input.clear()
    to_city_input.send_keys("Pune")

    # Departure- 4th July
    departure_date_input = driver.find_element(By.XPATH, "//input[@id='departure']")
    departure_date_input.clear()
    departure_date_input.send_keys("04/07/2023")

    # Return- 11th July
    return_date_input = driver.find_element(By.XPATH, "//input[@id='return']")
    return_date_input.clear()
    return_date_input.send_keys("11/07/2023")

    # Travelers & Class- 3 Adults
    travelers_class_input = driver.find_element(By.XPATH, "//input[@id='travellers']")
    travelers_class_input.click()
    adults_input = driver.find_element(By.XPATH, "//li[@data-cy='adults-3']")
    adults_input.click()

    # Click on Search
    search_button = driver.find_element(By.XPATH, "//a[@data-cy='search']")
    search_button.click()

    # Wait for the search results page to load
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-cy='flightItem']")))

    # Select "Non Stop" and "Late Departures" as filters from popular filters
    non_stop_filter = driver.find_element(By.XPATH, "//label[@for='filter_stop-0']")
    non_stop_filter.click()
    late_departures_filter = driver.find_element(By.XPATH, "//label[@for='filter_departure-2']")
    late_departures_filter.click()

    # Select "Indigo" as filters from Airlines filters
    indigo_filter = driver.find_element(By.XPATH, "//label[@for='filter_airline-6']")
    indigo_filter.click()

    # Move the One way price slider to the slight lt
    slider_handle = driver.find_element(By.XPATH, "//div[@id='price_slider']/span[@class='irs-slider single']")
    driver.execute_script("arguments[0].setAttribute('style', 'left: 80%;')", slider_handle)

    # Validate if at least one flight is visible
    flight_items = driver.find_elements(By.XPATH, "//div[@data-cy='flightItem']")
    if len(flight_items) > 0:
        print("At least one flight is visible.")
    else:
        print("No flights are visible.")
# Run the test cases and generate the report
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FlipkartTest)
    test_runner.run(suite)
    report_file.close()
