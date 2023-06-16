from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the demoqa website
driver.get("https://demoqa.com/")

# Click on "Alerts, Frame & Windows" link
driver.find_element(By.XPATH, "//div[text()='Alerts, Frame & Windows']").click()

# Click on "Alerts" link
driver.find_element(By.XPATH, "//span[text()='Alerts']").click()

# Click on "Click me" button for simple alert
driver.find_element(By.XPATH, "//button[text()='Click me']").click()

# Switch to the alert and accept it
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.accept()

# Click on "Click me" button for delayed alert
driver.find_element(By.XPATH, "//button[text()='Click me']").click()

# Wait for the alert to appear
WebDriverWait(driver, 10).until(EC.alert_is_present())

# Switch to the alert and accept it
alert = driver.switch_to.alert
alert.accept()

# Click on "Click me" button for confirm box
driver.find_element(By.XPATH, "//button[text()='Click me']").click()

# Wait for the confirm box to appear
WebDriverWait(driver, 10).until(EC.alert_is_present())

# Switch to the confirm box and accept it
confirm = driver.switch_to.alert
confirm.accept()

# Validate if the selected option is appearing
selected_option = driver.find_element(By.XPATH, "//p[@id='confirmResult']")
assert selected_option.text == "You selected Ok"

# Click on "Click me" button for prompt box
driver.find_element(By.XPATH, "//button[text()='Click me']").click()

# Wait for the prompt box to appear
WebDriverWait(driver, 10).until(EC.alert_is_present())

# Switch to the prompt box, send keys, and accept it
prompt = driver.switch_to.alert
prompt.send_keys("John Doe")
prompt.accept()

# Validate if the given name is appearing
given_name = driver.find_element(By.XPATH, "//p[@id='promptResult']")
assert given_name.text == "You entered John Doe"

# Close the browser
driver.quit()
