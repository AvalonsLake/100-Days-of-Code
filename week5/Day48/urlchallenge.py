from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.CSS_SELECTOR, "input[name='fName']")

last_name = driver.find_element(By.CSS_SELECTOR, "input[name='lName']")

email = driver.find_element(By.CSS_SELECTOR, "input[name='email']")

# ========== auto typing ========== #

first_name.send_keys("Talison")

last_name.send_keys("McLennon")

email.send_keys("talennon@mail.com")

sign_up_btn = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up_btn.click()