import requests
from datetime import datetime

#### SETTING UP A USER ACCOUNT ON PIXELA ####################

username = "shabnam"
token = "ugdciewfuqyiued"
graph_id = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Uncomment to create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": graph_id,
    "name": "Running",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": token
}

# Uncomment to create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

today = datetime.now()

pixel_data = {
    "date": today.strftime(("%Y%m%d")),
    "quantity": input("How many Km did you run today? "),
}

updated_data = {
    "quantity": "10",
}

response = requests.post(url=pixel_creation, json=pixel_data, headers=headers)
print(response.text)

pixel_updating = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime(('%Y%m%d'))}"

# response = requests.put(url=pixel_updating, json=updated_data, headers=headers)
# print(response.text)

pixel_deleting = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{today.strftime(('%Y%m%d'))}"

# response = requests.delete(url=pixel_deleting, json=updated_data, headers=headers)
# print(response.text)