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

# ---------- Create Pixel ---------- #

pixel_endpoint = f"{graph_endpoint}/{graph_id}"

graph_pixel = {
    "date": today.strftime("%Y-%m-%d"),
    # "date": "20260115",
    "quantity": "12"
}

# response = requests.post(url=pixel_endpoint, json=graph_pixel, headers=headers)
# print(response.text)

# ---------- Update Pixel ---------- #

update_pixel_ep = f"{pixel_endpoint}/20250115"

update_pixel = {
    "quantity": "3"
}

# response = requests.put(url=update_pixel_ep, json=update_pixel, headers=headers)
# print(response.text)

# ---------- Delete Pixel ---------- #

del_pix_endpoint = f"{pixel_endpoint}/20260115"

response = requests.delete(url=del_pix_endpoint, headers=headers)
print(response.text)