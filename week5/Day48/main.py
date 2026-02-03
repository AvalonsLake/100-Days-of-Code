from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# ============ Setting Up the driver ============ #
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")


driver.implicitly_wait(3)


# ============ try to find language option ============ #
print("clicking the language option")
try:
    language_select = driver.find_element(By.ID, "langSelect-EN")
    language_select.click()
    print("loading")
    sleep(3)
except NoSuchElementException:
    print("couldn't find the language button")

cookie = driver.find_element(By.ID, "bigCookie")
cookie.click()
sleep(1)


# ========== Timers ========== #
wait_time = 5
timeout = time() + wait_time
end_run = time() + 60 * 5


click = True
while click:
    cookie.click()
    if time() > timeout:
        try:
            # ========== Grabbing the total cookie count ========== #
            try:
                cookie_count = driver.find_element(By.ID, "cookies").text
                cookie_list = cookie_count.split()
                cookies = int(cookie_list[0])
            except:
                print("Cookie not found")

            # ========== Grabbing the upgrades  ========== #
            try:
                upgrades = driver.find_elements(By.CSS_SELECTOR, ".upgrade")
                most_expensive_upgrade = None
                for upgrade in reversed(upgrades):
                    if "enabled" in upgrade.get_attribute("class"):
                        most_expensive_upgrade = upgrade
                        break

                if most_expensive_upgrade:
                    most_expensive_upgrade.click()
            except:
                print("there was an error buying the upgrades")

            # ========== Grabbing the buldings  ========== #
            products = driver.find_elements(By.CSS_SELECTOR, ".product")

            most_expensive_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    most_expensive_item = product
                    if most_expensive_item:
                        most_expensive_item.click()
                        print(f"Bought a {most_expensive_item.text}")
                    # break



        except (NoSuchElementException, ValueError):
            print("couldn't find the product or cookies")

        timeout = time() + wait_time
    if time() > end_run:
        click = False
        try:
            cookie_count = driver.find_element(By.ID, "cookies").text
            print(f"final result {cookie_count}")
        except NoSuchElementException:
            print("couldn't find the final cookie count")



# driver.quit()