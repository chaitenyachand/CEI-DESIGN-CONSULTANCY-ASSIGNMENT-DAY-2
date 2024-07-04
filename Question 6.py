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

# Number of retries
max_retries = 3

# Collect 100 records of ISS location data
for _ in range(100):
    success = False
    retries = 0
    
    while not success and retries < max_retries:
        try:
            # Send a GET request to the API endpoint
            response = requests.get(url)
            
            # Check if the request was successful
            response.raise_for_status()
            
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
            
            success = True  # Set success flag to True
            
        except requests.exceptions.RequestException as e:
            retries += 1
            print(f"Attempt {retries} failed: {e}")
            time.sleep(1)  # Wait before retrying
    
    if not success:
        print(f"Failed to retrieve data after {max_retries} attempts. Exiting.")
        break

# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv("iss_location_data.csv", index=False)

print("Data collection complete. The data has been written to 'iss_location_data.csv'.")

