import requests
from datetime import datetime
import os

AGE = 23
GENDER = "male"
HEIGHT = 185
WEIGHT = 93

# ---------- Exercise API ---------- #

exercise_ep = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_app_id = os.environ["APP_ID"]
exercise_app_key = os.environ["APP_KEY"]

headers = {
    "x-app-id": exercise_app_id,
    "x-app-key": exercise_app_key
}

# ---------- Sheety API ---------- #

sheety_ep = os.environ["SHEETY_ENDPOINT"]
token = os.environ["TOKEN"]

bearer_header = {
    "Authorization": f"Bearer {token}"
}


exercise = input("So, what exercises did you do today? ")

exercise_params = {
    "query": exercise,
    "age": AGE,
    "gender": GENDER,
    "height_cm": HEIGHT,
    "weight_kg": WEIGHT,
}


response = requests.post(url=exercise_ep, json=exercise_params, headers=headers)
result = response.json()
print(result)

current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheety_params = {
        "sheet1": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(url=sheety_ep, json=sheety_params, headers=bearer_header)
    print(sheety_response.text)



