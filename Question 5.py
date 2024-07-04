# Write a Python program using the requests module to send a GET request to a given below url API endpoint and print the
#  a) Latitude
#  b) Longitude
#  c) timestamp
# (url : http://api.open-notify.org/iss-now.json)

import requests

# API endpoint URL
url = "http://api.open-notify.org/iss-now.json"

# Send a GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    json_data = response.json()
    
    # Extract the latitude, longitude, and timestamp
    latitude = json_data["iss_position"]["latitude"]
    longitude = json_data["iss_position"]["longitude"]
    timestamp = json_data["timestamp"]
    
    # Print the latitude, longitude, and timestamp
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print(f"Timestamp: {timestamp}")
else:
    # Print an error message if the request was not successful
    print(f"Failed to retrieve data: {response.status_code}")

# OUTPUT

# Latitude: -43.0004
# Longitude: -62.1206
# Timestamp: 1720107690
