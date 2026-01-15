import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "qwertyaslkdjfhlasdj"
USER = "thatguy222"
graph_id="graph1"

today = datetime.today()

headers = {
    "X-USER-TOKEN": TOKEN,
}

# ---------- Create Account ---------- #

user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ---------- Create Graph ---------- #

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Sketching Graph",
    "unit": "Sketches",
    "type": "int",
    "color": "shibafu"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ---------- Update Pixel ---------- #
def update_pixel():
    date = input("What date would you like to update? [YYYYMMDD] ").lower()
    amount = input("How many sketches did you do that day? ")
    update_pixel_ep = f"{pixel_endpoint}/{date}"

    update_pixel = {
        "quantity": amount
    }

    response = requests.put(url=update_pixel_ep, json=update_pixel, headers=headers)
    print(response.text)

# ---------- Delete Pixel ---------- #
def delete_pixel():
    date = input("What date do you want to delete? [YYYYMMDD] ").lower()
    del_pix_endpoint = f"{pixel_endpoint}/{date}"

    response = requests.delete(url=del_pix_endpoint, headers=headers)
    print(response.text)

# ---------- Create Pixel ---------- #

pixel_endpoint = f"{graph_endpoint}/{graph_id}"
run = True
while run:
    amount = input("How many sketches did you do today? ")
    if amount == "update":
        update_pixel()
    elif amount == "delete":
        delete_pixel()
    elif amount == "exit":
        run = False
    else:
        graph_pixel = {
            "date": today.strftime("%Y%m%d"),
            # "date": "20260115",
            "quantity": amount
        }

        response = requests.post(url=pixel_endpoint, json=graph_pixel, headers=headers)
        print(response.text)