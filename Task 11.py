from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Start a new instance of Chrome webdriver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://jqueryui.com/droppable/")

# Switch to the iframe containing the draggable element
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

# Locate the draggable element
draggable = driver.find_element(By.ID, "draggable")

# Locate the droppable element
droppable = driver.find_element(By.ID, "droppable")

# Perform drag and drop operation using ActionChains
actions = ActionChains(driver)
actions.drag_and_drop(draggable, droppable).perform()

# Wait for a while to see the result
time.sleep(5)

# Close the browser
driver.quit()
