from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()

# ========== Setting up the Driver ========== #

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Setting up a chrome profile for the Bot
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(os.getenv("GYM_URL"))

# ========== Account Details ========== #

gym_email = os.getenv("GYM_EMAIL")
gym_pass = os.getenv("GYM_PASSWORD")
# NOTE: use your own gym membership details here

# ========== Bot Stats ========== #
booked_classes = 0
waitlisted_classes = 0
already_registered_classes = 0
processed_classes = 0
# attempt stats
login_attempts = 1
booking_attempts = 1

# ========== Login ========== #
def login():
    global login_attempts
    WebDriverWait(driver, 3)
    # click the login btn
    print(f"Logging in... attempt: {login_attempts}")
    driver.find_element(By.ID, "login-button").click()

    # Find the inputs for email and password
    WebDriverWait(driver, 3)
    email = driver.find_element(By.ID, "email-input")
    password = driver.find_element(By.ID, "password-input")
    email.clear()
    password.clear()

    # fill in the Email and Password fields
    email.send_keys(gym_email)
    password.send_keys(gym_pass)

    # Submit the login credentials
    driver.find_element(By.ID, "submit-button").click()

    # Check that the Login was successful
    try:
        verify = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "schedule-page")))
        print("Logged in successfully")
        book_classes()
    except:
        print("Login failed")
        login_attempts += 1
        retry("login")


# ========== Book a class ========== #
def book_classes():
    global booking_attempts
    global booked_classes, waitlisted_classes, processed_classes, already_registered_classes
    print(f"Booking classes... Attempt: {booking_attempts}")

    # grabbing all classes
    classes = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

    for class_ in classes:
        try:
            day_group = class_.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
            day_title = day_group.find_element(By.TAG_NAME, "h2").text
            if "Tue" in day_title or "Thu" in day_title:
                # see if 6pm class
                time_text = class_.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
                if "6:00 PM" in time_text:
                    # Grab the class details
                    class_name = class_.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
                    # Grab the "Book Class" Btn
                    book_btn = class_.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
                    processed_classes += 1
                    # Check if class is already booked or on waitlist
                    if "booked" in book_btn.get_attribute("class"):
                        print(f"{class_name} is Already Booked on {day_title} at {time_text.replace('Time: ', '')}")
                        already_registered_classes += 1
                    elif "waitlisted" in book_btn.get_attribute("class"):
                        print(f"You are already waitlisted for {class_name} on {day_title} at {time_text.replace('Time: ', '')}")
                        already_registered_classes += 1
                    else:
                        if "waitlist" in book_btn.get_attribute("class"):
                            book_btn.click()
                            print(f"✓ Joined the waitlist for: {class_name} on {day_title} at {time_text.replace('Time: ', '')}")
                            waitlisted_classes += 1
                        else:
                            book_btn.click()
                            print(f"✓ Booked: {class_name} on {day_title} at {time_text.replace('Time: ', '')}")
                            booked_classes += 1
        except:
            print("booking class failed")
            booking_attempts += 1
            retry("booking")

# ========== Retry Function ========== #
def retry(type):
    if type == "login":
        login()
    if type == "booking":
        book_classes()

login()
# ========== Print the Bots Stats ========== #
print(f"--- BOOKING SUMMARY --- \n"
      f"Classes Booked: {booked_classes} \n"
      f"Waitlists Joined: {waitlisted_classes} \n"
      f"Already Booked or Waitlisted: {already_registered_classes} \n"
      f"Total Tuesday/Thursday 6pm  classes: {processed_classes}")

# ========== Verify the Classes were Booked ========== #

# navigate to "My Bookings" Page
driver.find_element(By.ID, "my-bookings-link").click()
# check the confirmed bookings
confirmed_classes = driver.find_elements(By.CSS_SELECTOR, "#confirmed-bookings-section div[id^='booking-card-']")
confirmed_bookings = len(confirmed_classes)

# check the Waitlist
confirmed_waiting = driver.find_elements(By.CSS_SELECTOR, "#waitlist-section div[id^='waitlist-card-']")
confirmed_waitlist = len(confirmed_waiting)
print("Verifying your classes...")
# check if the confirmed classes match the amount of processed classes
if confirmed_bookings + confirmed_waitlist == processed_classes:
    print("All classes booked successfully!")
else:
    print("Some classes failed to be booked")