from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
service = Service(executable_path='C:\Program Files\Chrome Driver\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)


# Navigate to makemytrip.com
driver.get("https://www.makemytrip.com/")

# Wait for the page to load
wait = WebDriverWait(driver, 10)
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

# Close the browser
driver.quit()
