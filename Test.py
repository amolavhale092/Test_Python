#print("Hello, This is the test python run.")
#print("It's Dev to MO Movement Test.")

import requests

# Define the API endpoint
url = "https://fake-json-api.mock.beeceptor.com/users"

# Make the GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    for i in range(10):
        print("ID:", data[i]['id'])
        print("Username:", data[i]['username'])
        print("Company:", data[i]['company'])
        print("Name:", data[i]['name'])
        print("Email:", data[i]['email'])
    

else:
    print("Failed to fetch data. Status code:", response.status_code)
