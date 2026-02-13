from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv
import pickle
import os
load_dotenv()

# ========== Setting up the Driver ========== #

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(os.getenv("URL"))

WebDriverWait(driver, 15)

accept_btn = driver.find_element(By.CSS_SELECTOR, ".My(8px) button")
accept_btn.click()