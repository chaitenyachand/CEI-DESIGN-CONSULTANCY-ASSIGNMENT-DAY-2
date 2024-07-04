# Write a Python program that write data in csv file using Pandas of ISS location with timestamp min 100 records
# use this url to get the data of ISS
# ( url : http://api.open-notify.org/iss-now.json)

import requests
import pandas as pd
import time

# API endpoint URL
url = "http://api.open-notify.org/iss-now.json"

# List to store ISS location data
data = []

# Collect 100 records of ISS location data
for _ in range(100):
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
        
        # Append the data to the list
        data.append({
            "timestamp": timestamp,
            "latitude": latitude,
            "longitude": longitude
        })
        
        # Print a message indicating progress
        print(f"Record {_+1}: Timestamp: {timestamp}, Latitude: {latitude}, Longitude: {longitude}")
    
    else:
        # Print an error message if the request was not successful
        print(f"Failed to retrieve data: {response.status_code}")
    
    # Wait for a short interval before the next request to avoid overwhelming the API server
    time.sleep(1)  # 1 second delay

# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv("iss_location_data.csv", index=False)

print("Data collection complete. The data has been written to 'iss_location_data.csv'.")
