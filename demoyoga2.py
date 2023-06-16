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

# Click on "Modal dialogs" link
driver.find_element(By.XPATH, "//span[text()='Modal Dialogs']").click()

# Click on "Small modal" button
driver.find_element(By.XPATH, "//button[text()='Small modal']").click()

# Validate the content of the small modal
small_modal_content = driver.find_element(By.XPATH, "//div[@id='example-modal-sizes-title-sm']")
assert small_modal_content.text == "Small Modal"

# Click on "Close" button for the small modal
driver.find_element(By.XPATH, "//button[text()='Close']").click()

# Click on "Large modal" button
driver.find_element(By.XPATH, "//button[text()='Large modal']").click()

# Validate the content of the large modal
large_modal_content = driver.find_element(By.XPATH, "//div[@id='example-modal-sizes-title-lg']")
assert large_modal_content.text == "Large Modal"

# Click on "Close" button for the large modal
driver.find_element(By.XPATH, "//button[text()='Close']").click()

# Close the browser
driver.quit()
