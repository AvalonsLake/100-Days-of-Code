from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# === go to wikipedia === #
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_elements(By.CSS_SELECTOR, "#articlecount li a[title='Special:Statistics']")

article_stats = [stat.text for stat in article_count]

print(f"The amount of active editors on Wikipedia right now is {article_stats[0]}")
print(f"The amount of articles on Wikipedia right now is {article_stats[1]}")

driver.quit()